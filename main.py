import telebot
from threading import Thread
from flask import Flask

TOKEN = '8743111071:AAH4kh9suBgGR9YG3ZTz8a9_v74M-T9qP4U'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 أبشرك يا بدر.. البوت شغال الحين 24 ساعة!")

app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if name == "__main__":
    keep_alive()
    bot.infinity_polling()
