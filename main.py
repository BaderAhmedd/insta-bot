import telebot
import requests
import time
from threading import Thread
from flask import Flask

# التوكن الخاص بك
TOKEN = '8743111071:AAH4kh9suBgGR9YG3ZTz8a9_v74M-T9qP4U'
bot = telebot.TeleBot(TOKEN)
monitored = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 البوت يعمل الآن بنجاح على السيرفر 24/7")

@bot.message_handler(commands=['add'])
def add(message):
    try:
        user = message.text.split()[1].replace('@', '')
        monitored[user] = message.chat.id
        bot.reply_to(message, f"✅ بدأ رصد الحساب: @{user}")
    except:
        bot.reply_to(message, "❌ خطأ! استخدم الأمر كذا: /add user")

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if name == "__main__":
    keep_alive()
    print("Bot is starting...")
    bot.infinity_polling()
