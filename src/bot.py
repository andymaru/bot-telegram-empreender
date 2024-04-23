from dotenv import load_dotenv

import os
import telebot

load_dotenv()

API_KEY_TELEGRAM = os.getenv("API_KEY_TELEGRAM")

bot = telebot.TeleBot(API_KEY_TELEGRAM)

print("Bot has been started")

@bot.message_handler(commands=["cardapio"])
def send_menu(message):
    text = """
        Os seguintes sanduíches estão disponíveis:

        1) Hamburguer de Siri
        Tem siri

        2) Hamburguer de Frango
        Tem frango

        3) Hamburguer de Carne
        Tem carne

        Digite a opção desejada:
    """

    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    user_first_name = message.from_user.first_name

    text = f"""
        Seja bem-vindo {user_first_name} ;)

        Vocẽ está no bot da Pizzaria da Boa
        Onde tudo de bom você encontra aqui

        https://google.com.br/

        Horário de funcionamento
        15h às 23h

        Comandos
        /cardapio
        /pedido
        /avalir
    """

    bot.reply_to(message, text)


bot.infinity_polling()
