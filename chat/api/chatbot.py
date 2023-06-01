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
