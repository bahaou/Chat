from frappe.core.doctype.user.user import User
import frappe



class CustomUser(User):
	@frappe.whitelist()
	def before_insert(self):
		email=self.email
		rooms=frappe.db.get_all("Chat Room",filters={"members":["like","%"+email+"%"],"chatgpt":1})
		if len(rooms)>0:
			return
		room=frappe.new_doc("Chat Room")
		room.room_name=self.email+" ChatGpt"
		room.type="Direct"
		room.members="businessplus@slnee.com, "+email
		room.chatgpt=1
		room.insert()
