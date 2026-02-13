import os
import telebot
import google.generativeai as genai

# CONFIGURACIÓN
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GOOGLE_API_KEY = "AIzaSyAx-9fje-gQS0DL-8J19ZrNQ68-PBITVmc"

# Inicializamos la IA
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicializamos el Bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola, socio! Soy tu IA personalizada. Ahora ya soy inteligente y puedo responderte lo que quieras. ¿En qué te ayudo hoy?")

@bot.message_handler(func=lambda message: True)
def chat_with_ia(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Dame un segundo, estoy procesando mucha información...")

if __name__ == "__main__":
    bot.infinity_polling()

