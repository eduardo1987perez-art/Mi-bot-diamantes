import os
import telebot

# Aquí el bot lee el TOKEN que pusiste en Render
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Tu bot de diamantes está encendido y funcionando perfectamente. 💎")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Recibí tu mensaje, pronto tendré más funciones.")

print("Bot en marcha...")
bot.infinity_polling()
