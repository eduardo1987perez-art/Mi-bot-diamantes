import os
import telebot
import google.generativeai as genai
from flask import Flask
import threading

# 1. CONFIGURACIÓN DE SERVIDOR PARA RENDER
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot vivo y funcionando", 200

# 2. CONFIGURACIÓN DE LLAVES (Ahora coinciden con Render)
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# Inicializamos la IA
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicializamos el Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola, socio! Soy tu IA personalizada. Ahora ya soy inteligente y puedo responderte lo que quieras. ¿En qué te ayudo hoy?")

@bot.message_handler(func=lambda message: True)
def chat_with_ia(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Dame un segundo, estoy procesando...")

# 3. LANZAMIENTO
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Esto arranca el bot en un hilo y Flask en otro para que Render esté feliz
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
