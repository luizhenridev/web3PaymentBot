import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
#from services.goog import main
from prompts.superhero import context
from prompts.intention import intention
from io import BytesIO
from PIL import Image
import base64

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY=os.environ.get("REQUESTER_TOKEN")
LINK = os.environ.get("LINK")
LINKIMAGE = os.environ.get("LINKIMAGE")
LINKAUDIO = os.environ.get("LINKAUDIO")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def gen(text, userId ,id_model = "gpt-4", max_tokens = 1000):
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : context},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.2
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]

    
    return responseMessage

def summarize(text, id_model = "gpt-4", max_tokens = 100):
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : summarize.contextSummarize},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.0
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage

def intentions(text = "Como você pode me ajudar?", id_model = "gpt-4", max_tokens = 1000):

    body_message = {
        "model" : id_model,
        "messages" : [{"role" : "system", "content" : intention},
                      {"role" : "user", "content" : text}],
        "max_tokens" : max_tokens,
        "temperature" : 0.2
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]

    print(responseMessage)
    return responseMessage


def explorer(text, userId ,id_model = "gpt-4", max_tokens = 1000):

    context1 = """
CONTEXT: 
1. You are Aurora, the virtual assistant designed to help the user keep their financial organized
2. You will chat with the user - in Portuguese - 
4. Consider this to be your database
6. Based on your database answer financial advices
7. Just give advices when the user request
8. Give summarized answers above 100 tokens to avoid incomplete answers
9. Answer straight wit

### Examples
        NOTE: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Quanto eu gastei no mês de Janeiro?
            recommended answer:
            Você gastou um total de R$3.074,47 --- algo nesse sentido

        Example 2: 
            user message: 
            Me diga as áreas que eu mais gastei no mês de janeiro
            recommended answer:
            Imposto: Você gastou R$885,98 
            Educação: Você gastou R$778,66 
            Outros: Você gastou R$678,24 
            
 """
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : context1},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.2
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage


def genImage(text: str = "Hey spiderman take a photo from you right now, please like a selfie"):
    

    body_message = {
        "model": "dall-e-3",
        "prompt": text,
        "size": "1024x1024",
        "quality":"standard",
        "n": 1
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINKIMAGE, headers=headers,data=body_message )
    response = requisition.json()
    responseUrl= response['data'][0]['url']


    
    return responseUrl

def image_to_base64(image):
    # Convert a PIL Image to a base64-encoded string
    buffered = BytesIO()
    image.save(buffered, format="JPEG")  # You can adjust the format as needed
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    


def genAudio (text: str):
    body_message = {
        "model": "tts-1-hd",
        "input": text,
        "voice": "alloy",
        "response_format": "mp3",
        "speed": 1.0
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINKAUDIO, headers=headers,data=body_message )
    response = requisition.json()
    responseUrl= response['data'][0]['url']
    print(response)
    print(responseUrl)

if __name__ == '__main__':
    genImage()