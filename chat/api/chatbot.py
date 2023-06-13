import frappe
from frappe import _
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


#chatbot=ChatBot("Business Plus")
#chats=open("chat.txt","r").readlines()

def chatbot(question):
	
	chatbot=ChatBot("Business Plus")
	files=["conversations","computers"]
	all_chats=[]
	#for f in files:
	#	chats=open("../apps/chat/chat/api/data/"+f+".txt","r").readlines()
	#	all_chats=all_chats+chats
	#trainer=ListTrainer(chatbot)
	#trainer.train(all_chats)
	response=chatbot.get_response(question)
	return(response.text)


def train_chatbot(chat):
	chatbot=ChatBot("Business Plus")
	trainer=ListTrainer(chatbot)
	trainer.train(chat)

def train(main,answer,pos=[],gif=None,train=None):
	pos.append(main)
	chatbot=ChatBot("Business Plus")
	trainer=ListTrainer(chatbot)
	for p in pos:
		trainer.train([p,answer])
	if gif:
		settings=frappe.get_doc("Chat Settings")
		for g in settings.gifs:
			if train==train:
				g.description=answer[:30]
				g.file=gif
				settings.save()
				frappe.db.commit()
				return
		new=settings.append("gifs",{})
		new.description=answer[:30]
		new.file=gif
		new.train=train
		settings.save()
	frappe.db.commit()
