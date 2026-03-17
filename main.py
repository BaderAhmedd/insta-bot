import telebot
import requests
import time
from threading import Thread
from flask import Flask

# التوكن حقك
TOKEN = '8743111071:AAH4kh9suBgGR9YG3ZTz8a9Wc-_nrAzLmlk'
bot = telebot.TeleBot(TOKEN)
monitored = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 الرادار الذكي شغال على السيرفر 24/7!\nأرسل /add واسم الحساب للمراقبة.")

@bot.message_handler(commands=['add'])
def add(message):
    try:
        user = message.text.split()[1].replace('@', '')
        monitored[user] = message.chat.id
        bot.reply_to(message, f"✅ تم تفعيل الرادار الذكي لـ @{user}")
    except:
        bot.reply_to(message, "❌ أرسل: /add username")

def check_loop():
    while True:
        for u, c in list(monitored.items()):
            try:
                url = f"https://www.instagram.com/{u}/"
                headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/104.1'}
                r = requests.get(url, headers=headers, timeout=20)
                if r.status_code == 200 and ("Followers" in r.text or "Posts" in r.text):
                    bot.send_message(c, f"🎊 أبشرك! حساب @{u} اشتغل الآن ✅")
                    del monitored[u]
            except: pass
        time.sleep(600)

app = Flask('')
@app.route('/')
def home(): return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

if name == "__main__":
    Thread(target=check_loop, daemon=True).start()
    Thread(target=run_web, daemon=True).start()
    bot.infinity_polling()
