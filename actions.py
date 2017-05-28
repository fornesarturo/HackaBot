from other_functions import *

def generateAnswer(text):
    if "hola" in text.lower():
        return "Hola, gusto en hablar contigo, aunque en realidad esté hardcodeado","text","options"
    if "GET_STARTED_PAYLOAD" in text:
        return "Hola, soy un Bot que procesa tus tramites, para proseguir haz click en algún botón o envía un mensaje","text","options"
    if "PAYLOAD_HELP" in text or "help" in text.lower():
        return "Hola, soy un Bot que procesa tus tramites, para proseguir haz click en algún botón o envía un mensaje","text","options"
    if "PAYLOAD_TRAMITE" in text or "trámite" in text.lower() or "tramite" in text.lower():
        return "Dame tu INE, anda, confía","text","options"
    if "PAYLOAD_RFC" in text or "rfc" in text.lower():
        r=requests.get("http://35.162.69.59:8080/api/ine/"+sender)
        if (r is not None):
            datamagic= json.dumps(r)
            decoded = json.loads(datamagic)
            nombre = str(decoded["message"]["fName"])
            apellido_paterno = str(decoded["message"]["lName"])
            apellido_materno = str(decoded["message"]["mName"])
            curp = str(decoded["message"]["curp"])
            year=str(year[4])+str(year[5])
            mes=str(year[6])+str(year[7])
            dia=str(year[8])+str(year[9])
            fecha="19"+year+"/"+mes+"/"+dia
            urlapi = "https://jfhe88-rfc-generator-mexico.p.mashape.com/rest1/rfc/get?apellido_materno="+ apellido_materno + "&apellido_paterno="+apellido_paterno+"&fecha="+fecha+"&nombre="+nombre+"&solo_homoclave=0"
            response = unirest.get(urlapi,
                headers={
                    "X-Mashape-Key": "frrZzTz5DRmshqCacX6WoXCV5CA3p1w4zQyjsnXNx21g4BiCEd",
                    "Accept": "application/json"
                    })
            data_string = json.dumps(response)
            decoded = json.loads(data_string)
            magia = str(decoded["data"]["rfc"])
            return "Tu RFC es "+magia,"text","options"
        else:
            return "Por favor oprime primero en trámite","text","options"
    return "Oops, no te entendí","text","options"

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
                timestamp = event['timestamp']
                sendMessage2DB(sender,text,timestamp)
                if event['message'].get('quick_reply'):
                    payload = event['message']['quick_reply']['payload']
                    answer,_type,quick_reply = generateAnswer(payload)
                elif not text:
                    attachment_type =  str(event['message']['attachments'][0]['type'])
                    if attachment_type == "image":
                        _url = event["message"]["attachments"][0]["payload"].get("url")
                        if isThisAnINE(_url):
                            sendIne2DB(sender,_url)
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

def log(text):
    print(str(text))
    sys.stdout.flush()
