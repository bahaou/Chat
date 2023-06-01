import frappe
from frappe import _
import requests




def response(content):
	content=content+" في سطرين"
	url = "https://openai80.p.rapidapi.com/chat/completions"
	error_message="I am sorry, ChatGPT is offline, pelase check chat SEttings or contact administration."
	error_message="أنا آسف ، لست متاحًا ، يرجى التحقق من إعدادات الدردشة أو الاتصال بالإدارة."
	time_out_error="انا اسف . يبدو أنني آخذ الكثير من الوقت للإجابة. حاول مرة اخرى"
	payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": content
		}
		]
	}
	settings=frappe.get_doc("Chat Settings")
	key=settings.rapidapi_key
	host=settings.rapidapi_host
	if not key or not host:
		return([_(error_message)]) 
	headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": host
	}
	response = requests.post(url, json=payload, headers=headers).json()
	print (response)
	try:
		tokens=int(response["usage"]["total_tokens"])+int(settings.total_tokens)
		settings.total_tokens=tokens
		settings.save()
		frappe.db.commit()
	except:
		pass
	if 'id' in response.keys():
		answers=[]
		try:
			for a in response["choices"]:
				answer=a["message"]["content"]
				answers.append(answer)
				if len(answers)>0:
					return(answers)
				return([_(time_out_error)])
		except:
			return([_(error_message)])
	try:
		if "The request to the API has timed out" in response["messages"]:
			return([_(time_out_error)])
	except:
		pass
	return([_(error_message)])
