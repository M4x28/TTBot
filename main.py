from keep_alive import *
from weatherAPI import *
from faceRecognition import *
from firstDetection import *
import emoji
import requests
import telebot
import os


info = '''
Howdy, how are you doing?\nHere are my features:\n-Weather /weather:\n
  send me your location with this format: [/weather city,country_code (ex. it)]\n
  or you can send me your location with maps\n
-CO2 Emissions: /co2emissions check the wordwide map!\n
- /recognition Send an Image for test my Object Detection script!!! (Low power due to the weak server)
'''

bot = telebot.TeleBot(os.environ['API_KEY'])
img = open('datawrapCO2Emissions.png', 'rb')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, info)

@bot.message_handler(commands=['recognition'])
def send_recognitionRequest(message):
	bot.send_message(message.chat.id, 'Finally! Now send me a photo and I\'ll do my best')

# Photo
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
  #print ('message.photo =', message.photo)
  fileID = message.photo[-1].file_id
  file_info = bot.get_file(fileID)
  #print ('file.file_path =', file_info.file_path)
  downloaded_file = bot.download_file(file_info.file_path)

  with open("image.jpg", 'wb') as new_file:
    new_file.write(downloaded_file)
  try:
    bot.send_photo(message.chat.id, getDetection(), "Result " + emoji.emojize(':beaming_face_with_smiling_eyes:'))
  except:
    pass

# DataWrapper CO2 emission
@bot.message_handler(commands=['co2emissions'])
def send_dataWrapperLink(message):
	bot.send_photo(message.chat.id, img,"Link to DataWrapper: https://datawrapper.dwcdn.net/UbFtQ/1/")

# Weather
@bot.message_handler(commands=['weather'])
def send_temperature(message):
  bot.send_chat_action(message.chat.id, 'find_location')
  bot.send_message(message.chat.id, 'Send me your location!')
  
	#bot.send_message(message.chat.id, getWeather(message.text[9:]))
  

# Location
@bot.message_handler(content_types=['location'])
def handle_location(message):
  bot.send_message(message.chat.id, getWeatherfromLocation(message.location.latitude, message.location.longitude))

keep_alive()
bot.polling()
