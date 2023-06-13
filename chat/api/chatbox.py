import frappe
from frappe import _
from chat.api.message import chatgpt
from chat.api.message import send

@frappe.whitelist(allow_guest=True)
def first_box(room_name):
	try:
		room=frappe.get_doc("Chat Room",room_name)
	except:
		return None
	if not room.chatgpt:
		return None
	boxes=frappe.db.get_all("Chat Boxes",filters={"parent_chat_boxes":"Business Plus"})
	if len(boxes)==0:
		return None
	boxes=[b["name"] for b in boxes]
	chats=frappe.db.get_all("Chat Message",filters={"room":room_name},fields=["content"])
	if False and (len(chats)==0 or chats[0]["content"]!="Please Select your issue type." ) :
		chatgpt(_("Please Select your issue type."),room_name)
	return boxes

@frappe.whitelist(allow_guest=True)
def next_box(box,room_name):
	send(_(box),frappe.session.user,room_name,frappe.session.user)
	answer=frappe.db.get_value("Chat Boxes",box,"answer")
	if answer:
		chatgpt(_(answer),room_name)
	boxes=frappe.db.get_all("Chat Boxes",filters={"parent_chat_boxes":box},fields=["name","is_group"])
	if len(boxes)==0:
		return None
	boxes=[b["name"] for b in boxes]
	description=frappe.db.get_value("Chat Boxes",box,"description")
	if description:
		chatgpt(_(description),room_name)
	return boxes
	
