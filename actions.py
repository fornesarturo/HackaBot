from other_functions import *

def generateAnswer(text):
    if "hola" in text.lower():
        return "Hola, gusto en hablar contigo, aunque en realidad esté hardcodeado","text","options"
    if "GET_STARTED_PAYLOAD" in text:
        return "Hola, soy un Bot que procesa tus tramites, para proseguir haz click en algún botón o envía un mensaje","text","welcome"
    if "PAYLOAD_HELP" in text:
        return "Hola, soy un Bot que procesa tus tramites, para proseguir haz click en algún botón o envía un mensaje","text","welcome"
    return "Dame tu INE, anda, confía","text","options"

class EntryManager(object):
    def __init__(self,entry):
        self.entry = entry
        self.message_list = []
        for event in entry['messaging']:
            if(event.get("postback") or event.get("message")):
                self.message_list.append(event)
    def answerEntry(self):
        def getAnswer(event):
            if event.get("message"):
                sender = event['sender']['id']
                text = event['message'].get('text')
                if event['message'].get('quick_reply'):
                    payload = event['message']['quick_reply']['payload']
                    answer,_type,quick_reply = generateAnswer(payload)
                if not text:
                    attachment_type =  str(event['message']['attachments'][0]['type'])
                    if attachment_type == "image":
                        if isThisanINE():
                            _url = event["message"]["attachments"][0]["payload"]["url"]
                            answer,_type,quick_reply = str(getUserInfo(sender))+str(_url),'text','options'
                        else:
                            answer,_type,quick_reply = "Looks like this is not an INE!",'text','options'
                    else:
                        answer,_type,quick_reply = 'Nice ' + str(event['message']['attachments'][0]['type']),'text','options'
                else:
                    answer,_type,quick_reply = generateAnswer(text)
                if "text" in _type:
                    return {'sender':sender,'user_text':text,'text':answer,'type':_type,'quick':quick_reply}
            if event.get("postback"):
                payload = event['postback']['payload']
                sender = event['sender']['id']
                answer,_type,quick_reply = generateAnswer(payload)
                return {'sender':sender,'user_text':payload,'text':answer,'type':_type,'quick':quick_reply}
        answer_list = map(getAnswer, self.message_list)
        return answer_list
