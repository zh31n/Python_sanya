import telebot
from telebot import types
import time
import datetime


bot = telebot.TeleBot("6676190461:AAH9U50OMC4vHFAz9ZeKUwBoX44UyGPRFFM")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '💬 Мемоцит - бот для чатов :)\n\n– отправьте сообщение чтобы\nсоздать мемоцит, ответьте\nна чьё-то сообщение\nкомандой /m и бот сделает\nмемоцит.\n\n#⃣ Другие команды, [инфа](https://telegra.ph/Instrukciya---Memocit-01-15)', parse_mode='Markdown', disable_web_page_preview=True)

@bot.message_handler(commands=['profile'])
def profile(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(
        text='🛠Стикеры', callback_data='test')
    item2 = types.InlineKeyboardButton(
        text='➕Создать свой мемоцит', callback_data='test')
    markup_inline.add(item1,item2)
    bot.send_message(message.chat.id, message.from_user.first_name+' '+'твой профиль 🙊\n\n-создано 0 цитат\n-место в топе:#1\n\n⬇️ Ещё можно редактировать свои стикерпаки',reply_markup=markup_inline)





bot.polling(none_stop=True)