import BotAmino
import giphy_client as gc
from giphy_client.rest import ApiException  
from BotAmino import BotAmino, Parameters
import urllib
import random
import os
import time
import requests
import sys

print("wait...")
client = BotAmino("jwevri9h@xojxe.com", "aaaa5555", deviceId = "170faa37a93d67616b2297a4d2a485bccfae8fac97a9572736d58665356a9b1f7ff978c88c4f92c706")



client.prefix = "/"  # set the prefix to /
client.wait = 4  # wait 4 sec before doing a new command

comid= 165549708

client.add_community(comid)
subclient = client.get_community(comid)
subclient.join_chatroom("6934ee2b-fe70-48c7-92a2-47b2e8b97d88")

@client.command()
def help(data):
  help = ("""Bot Help Menu
/startvc ~~~~~> to start Vc
/endvc ~~~~~> to end Vc                
/startVideo ~~~~~> start video                    
/bg ~~~~~> get background image
/gold ~~~~~> get some Golds """)
  data.subClient.send_message(data.chatId, message=help)

@client.command()
def startvc(data):
	client.start_vc(comId=data.comId,chatId=data.chatId)

@client.command()
def endvc(data):
	client.end_vc(comId=data.comId,chatId=data.chatId)

@client.command()
def startVideo(data):
  client.start_video_chat(comId=data.comId,chatId=data.chatId)

@client.command()
def bg(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
      filename = image.split("/")[-1]
      urllib.request.urlretrieve(image, filename)
      with open(filename, 'rb') as fp:
        data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")
        
@client.command()
def gold(data):
  with open('FB51D59A-65DD-4888-BD22-177D7DA9F57F.png', 'rb') as go:
    data.subClient.send_message(chatId=data.chatId, file=go, fileType="image")

@client.command()
def gif(data):
  api_instance = gc.DefaultApi()
  api_key = 'apna api key'
  query = data.message
  fmt = 'gif'
  response = api_instance.gifs_search_get(api_key,query,limit=1,offset=random.randint(1,10),fmt=fmt)
  gif = response.data[0]
  url= gif.images.downsized.url
  #print(url)

  urllib.request.urlretrieve(url,f"{data.message}.gif")
  with open(f"{data.message}.gif","rb") as file:
  	data.subClient.send_message(chatId=data.chatId,file=file,fileType="gif")
  	os.remove(f"{data.message}.gif")

	
client.launch()
print("ready")

