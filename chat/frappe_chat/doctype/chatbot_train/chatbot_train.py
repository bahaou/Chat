# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from chat.api.chatbot import train


class ChatBotTrain(Document):
	@frappe.whitelist()
	def on_update(self):
		pos=self.other_possibilities.split("\n")
		train(self.main_question,self.answer,pos,self.gif,self.name)
