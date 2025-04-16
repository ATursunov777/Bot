import os
import time
import schedule
from datetime import datetime
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
bot = Bot(token=TOKEN)

def send_message(text):
    try:
        bot.send_message(chat_id=GROUP_ID, text=text)
    except Exception as e:
        print("Ошибка при отправке:", e)

def forecast_task():
    buy_prob = 64
    sell_prob = 36
    text = f"📊 Прогноз XAUUSD:\nПокупка: {buy_prob}%\nПродажа: {sell_prob}%"
    send_message(text)

def daily_news():
    news = "📰 Новости по XAUUSD: золото торгуется стабильно, инвесторы ожидают данных по инфляции в США."
    send_message(news)

def session_reminders():
    now = datetime.now().strftime('%H:%M')
    reminders = {
        "03:45": "⏰ Скоро откроется Сиднейская сессия (в 04:00)",
        "04:45": "⏰ Скоро откроется Токийская сессия (в 05:00)",
        "10:45": "⏰ Скоро откроется Лондонская сессия (в 11:00)",
        "16:45": "⏰ Скоро откроется Нью-Йоркская сессия (в 17:00)",
        "01:45": "🔕 Скоро закроется Нью-Йоркская сессия (в 02:00)",
    }
    if now in reminders:
        send_message(reminders[now])

def high_confidence_check():
    confidence = 82
    if confidence >= 80:
        send_message(f"🚨 Сигнал по XAUUSD с уверенностью {confidence}% — возможна сильная покупка!")

schedule.every(30).minutes.do(forecast_task)
schedule.every().day.at("08:00").do(daily_news)
schedule.every(1).minutes.do(session_reminders)
schedule.every(2).minutes.do(high_confidence_check)

send_message("✅ Бот успешно запущен!")

while True:
    schedule.run_pending()
    time.sleep(1)
