import psycopg2
import telebot
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
key1 = telebot.types.InlineKeyboardButton (text='Дай цитату!')
keyboard1.add(key1)



bot = telebot.TeleBot("943087428:AAEoLmSLXJfsTHbkA-wRIEmhoGKb-8SPrxI")


def getQuote():
	conn = psycopg2.connect(user='admeen1337', password='aB1dxd9_s', dbname='bot_py',
							host='hwsrv-738030.hostwindsdns.com', port=5432)
	cur = conn.cursor()
	cur.execute('SELECT quote_text FROM quote ORDER BY random() limit 1')
	quote = cur.fetchall()
	return quote
	cur.close()
	conn.commit()
	conn.close()


def writeQuote(text):
	conn = psycopg2.connect(user='admeen1337', password='aB1dxd9_s', dbname='bot_py',
							host='hwsrv-738030.hostwindsdns.com', port=5432)
	cur = conn.cursor()
	cur.execute(f"INSERT INTO quote (quote_text) VALUES ('{text}')")
	cur.close()
	conn.commit()
	conn.close()


@bot.message_handler(func=lambda message: True)
def talk (message):
	if message.text == 'Дай цитату!':
		bot.reply_to(message, getQuote())
	elif message.text == 'Привет!':
		bot.send_message(message.chat.id, "Привет!", reply_markup=keyboard1)
	else:
		writeQuote(message.text)
		bot.reply_to(message, "Записал!")



bot.polling()



