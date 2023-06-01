# Copyright (c) 2021, codescientist703 and contributors
# For license information, please see license.txt
from chat.api.message import chatgpt
import frappe
import time
from chat.utils import update_room, is_user_allowed_in_room, raise_not_authorized_error
from chat.api.chatbot import chatbot
from frappe import _
from frappe.model.document import Document
from random import choice
from chat.api.chatgpt import response

class ChatMessage(Document):
	

	@frappe.whitelist()
	def after_insert(self):
		room=frappe.get_doc('Chat Room',self.room)
		if not room.chatgpt:
			return
		if self.sender_email=="businessplus@slnee.com":
			return
		if not self.content:
			return
		answers=response(self.content)
		#frappe.throw(str(answers))
		for a in answers:
			if a:
				chatgpt(a,room.name)


	@frappe.whitelist()
	def after_insertt(self):
		paper_game=["ورق","حجر","مقص"]
		room=frappe.get_doc('Chat Room',self.room)
		if not room.chatgpt:
			return
		if self.sender_email=="businessplus@slnee.com":
			return
		paper_sisors_game=paper_sisors(self.content)
		if paper_sisors_game:
			response=paper_sisors_game
		else:
			try:
				response=str(eval(self.content))
			except:
				name1=name(self.content)
				j=joke(self.content)
				if name1:
					response=name1
				else:
					if j:
						response=j
					else:
						response=chatbot(self.content)
		chatgpt(response,room.name)
		#update_room(room=room.name,last_message=response)
		#frappe.db.set_value("Chat Room",room.name,"last_message",response)


def joke(t):
	if "مزحة" in t or "نكتة" in t or "نكت" in t:
		jokes=open("../apps/chat/chat/jokes.txt",'r').readlines()
		return(choice(jokes))


def name(t):
	if "اسمك" in t or "ما إسمك" in t or "ما اسمك" in t or "من أنت" in t:
		try:
			name=frappe.get_doc('ChatBot Settings').chatbot_name
			answers=["أنا {}","إسمي {}","يمكنك مناداتي {}"]
		except:
			answers=["لا أعرف إسمي","لا أدري","لا أدري . من أنا ؟"]
		return(choice(answers).format(name))
	return None

def paper_sisors(t):
	paper_game=["ورق","حجر","مقص"]
	if t=="ورق" or t=="ورق ":
		answer=choice(paper_game)
		if answer=="مقص":
			response=answer+" ✂️ , "+win()
		elif answer=="ورق":
			response=answer+" ✋ , "+tie()
		else:
			response=answer+"✊, "+lose()
		time.sleep(1)
		return response
	elif t in ["حجر","حجر "]:
		answer=choice(paper_game)
		if answer=="مقص":
			response=answer+" ✂️ , "+lose()
		elif answer=="ورق":
			response=answer+"✋ , "+win()
		else:
			response=answer+" ✊ , "+tie()
		time.sleep(1)
		return response
	elif t in ["مقص","مقص "]:
		answer=choice(paper_game)
		if answer=="مقص":
			response=answer+ "✂️ , "+tie()
		elif answer=="ورق":
			response=answer+" ✋ , "+lose()
		else:
			response=answer+" ✊ , "+win()
		time.sleep(1)
		return response
	else:
		return None

def win():
	answers=["أجل، أنا ربحت "," أنا ربحت "," أنا ربحت ، حظا موفقا في المرة القادمة"]
	return(_(choice(answers)))
def lose():
	answers=["لا ، لقد خسرت","أنت ربحت","أنت الرابح"]
	return(_(choice(answers)))
def tie():
	answers=["تعادلنا.","إنه تعادل"]
	return(_(choice(answers)))
