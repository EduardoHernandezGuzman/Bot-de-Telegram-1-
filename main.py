import telebot
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Creación de los comandos básicos 
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a mi primer proyecto de bot de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /help - Obtiene ayuda sobre cómo usar el bot
    /about - Muestra información sobre este bot
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)


@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "¡Claro! Estoy aquí para ayudarte. Si tienes alguna pregunta o necesitas asistencia, no dudes en decírmelo. Estoy aquí para hacer que tu experiencia con este bot sea lo más fácil y agradable posible.")


@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte en tus tareas diarias.
    
    Este bot fue creado como parte de mi primer proyecto de desarrollo de un bot de Telegram.
    """
    bot.reply_to(message, about_text)


if __name__ == "__main__":
    bot.polling(none_stop=True)