import telebot
from telebot import types
#token = 1797764380:AAFqgur1Uu5xP0Ipq8FP7fzZPUX_Hhl0nEs
name = ""
surname = ""
age = 0

bot = telebot.TeleBot("1983412834:AAFmTrEzEa1HOWIoGvRspNn6zLf3wQzTJ10")
@bot.message_handler(commands=["start","help"])#старт бота на какие команды будет отвечать
def send_welcome(message):#сообщение бота привественное или любое другое
	bot.reply_to(message, "нах запустил?")#само сообщение

@bot.message_handler(func=lambda m: True)#лямбда (просто запомнить)
def echo_all(message):#функция для эхо бота дублирует сообщения
	if message.text == "ку":#сообщение пользователя 
				bot.reply_to(message, "привет ")#ответ бота // chto

	elif message.text == "как дела?":#повтор предыдущего цикла
   			 bot.reply_to(message, "ок")#сообщение бота которое будет выводится если польз 
   			 #напишет предыдущее сообщение 
		#bot.reply_to(message, message.text)
		#реплики так же можно добовлять командой if и elif неважно какая все ровно ответы будут
	elif message.text == "/reg":
			 bot.send_message(message.from_user.id,"Привет, давай познакомимся? Как тебя зовут?")
			 bot.register_next_step_handler(message, reg_name)
def reg_name(message):
	global name 
	name = message.text
	bot.send_message(message.from_user.id,"Назови свою фамилию?")	
	bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
	global surname 
	surname = message.text
	bot.send_message(message.from_user.id,"сколько лет?")	
	bot.register_next_step_handler(message, reg_age)

def reg_age(message):
	global age
	#age = message.text
	while age == 0:
		try:
			age = int(message.text)
		except Exception:
			bot.send_message(message.from_user.id,"Вводи цифрами")

	bot.register_next_step_handler(message, reg_ok)

def any_msg(message):
    banlist = redis.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button = types.InlineKeyboardButton(text="URL", url="https://ya.ru")
        callback_button = types.InlineKeyboardButton(text="Callback", callback_data="test")
        switch_button = types.InlineKeyboardButton(text="Switch", switch_inline_query="Telegram")
        keyboard.add(url_button, callback_button, switch_button)
        bot.send_message(message.chat.id, "Please Choose One :D", reply_markup=keyboard)
        
bot.polling()#команда для запуска бота (обьзательно) // 