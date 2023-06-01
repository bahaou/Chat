# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from chat.api.chatbot import train_chatbot


class ChatBotSettings(Document):
	@frappe.whitelist()
	def train(self):
		chat=self.conversations.split("\n")
		train_chatbot(chat)
