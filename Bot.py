pip install pyTelegramBotAPI
pip install requests

import requests

def get_crypto_price(crypto):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={crypto}"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "1a9d79a6-2576-4a9b-894d-5bd818028a12"
    }
    response = requests.get(url, headers=headers).json()
    price = response["data"][crypto]["quote"]["USD"]["price"]
    return price

@bot.message_handler(func=lambda message: "fiyat" in message.text.lower())
def send_crypto_price(message):
    crypto = message.text.split()[0].upper()
    price = get_crypto_price(crypto)
    bot.send_message(message.chat.id, f"{crypto} fiyatı: ${price}")

import telebot

bot = telebot.TeleBot("5868304306:AAGgyOjhCxkL8PtsTkZVIRHcfPD5a53wAWw")
