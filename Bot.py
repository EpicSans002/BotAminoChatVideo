import BotAmino
from BotAmino import BotAmino, Parameters
import urllib
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
def gif_search(message=None, messageId=None, authorId=None, author=None):
  search = message
  response = requests.get(
      'http://api.giphy.com/v1/gifs/search?q=' + search +
	     '&api_key=1jdqvfFwB2Vf12z6ZJ72sqkYm1yz0VVM&limit=10')
  #print(response.text)
  data = json.loads(response.text)
  gif_choice = random.randint(0, 9)
  image = data['data'][gif_choice]['images']['original']['url']
  print("URL", image)
  if image is not None:
    print(image)
    filename = image.split("/")[-1]
    urllib.request.urlretrieve(image, filename)
    with open(filename, 'rb') as fp:
      subClient.send_message(chatId, file=fp, fileType="gif")
      print(os.remove(filename))

	
client.launch()
print("ready")

