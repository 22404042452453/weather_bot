import telebot
from my_token import token1
from stepic3 import get_weather


bot = telebot.TeleBot(token1)

# commands of bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здравствуй,пользователь\n"
									  "Введите название своего города :")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "Этот бот может помочь узнать погоду в твоем городе на сегодня\n"
									  "Необходимо ввести название города:")

#basic function
@bot.message_handler(content_types= ['text'])
def send_weather(message):
	bot.send_message(message.chat.id,get_weather(message.text))


bot.polling(none_stop=True)
