from telebot import *
from telebot import types
import sqlite3
import time
import os.path
import requests
from bs4 import BeautifulSoup
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',

]
bot = telebot.TeleBot('5494614484:AAHiCjDUB0jkAIPZeg6Oj07Re43MJtcCf9s')

options = Options()
options.headless = True

def janri(janr):
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    url = f'https://wr.lordfilm7.link/film2/{janr}/'
    page = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")
    name = page.find("div", class_="th-item").text.split()
    name = ' '.join(name)
    Link_STR = page.find("div", class_="th-item")
    Link_STR = Link_STR.find("a", class_="th-in with-mask").get('href')

    return [name, Link_STR]




@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard1.row('Связаться с автором✉️', 'Функциии⚙️')
    bot.send_message(message.chat.id, 'Привет, чем тебе помочь?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Функциии⚙️':
        keyboard2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button3 = types.KeyboardButton('Личный профиль📖')
        button4 = types.KeyboardButton('Поиск фильма🎬')
        keyboard2.add(button3, button4)
        keyboard2.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Секунду... ', reply_markup=keyboard2)

    elif message.text == 'Связаться с автором✉️':
        bot.send_message(message.chat.id, 'https://t.me/weuoxs')


    elif message.text == 'Вернуться⬅️':
        keyboard11 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard11.row('Связаться с автором✉️', 'Функциии⚙️')
        bot.send_message(message.chat.id, 'Привет, чем тебе помочь?', reply_markup=keyboard11)

    elif message.text == 'Личный профиль📖':
        keyboard3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button5 = types.KeyboardButton('Избранное⭐')
        keyboard3.add(button5)
        keyboard3.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Выберите: ', reply_markup=keyboard3)

    elif message.text == 'Поиск фильма🎬':
        keyboard4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button7 = types.KeyboardButton('По фильтру📖')
        button8 = types.KeyboardButton('Случайный фильм🎲')
        keyboard4.add(button7)
        keyboard4.add(button8)
        keyboard4.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Выберите: ', reply_markup=keyboard4)

    elif message.text == 'Избранное⭐':
        with open('text1.txt', 'r', encoding='UTF-8') as file:
            text1 = file.readline()
        bot.send_message(message.chat.id, f'Избранные фильмы:\n{text1}' )

    elif message.text == 'По фильтру📖':
        keyboard5 = types.ReplyKeyboardMarkup()
        callback_button1 = types.KeyboardButton('Боевики')
        callback_button2 = types.KeyboardButton('Детективы')
        callback_button4 = types.KeyboardButton('Комедии')
        callback_button6 = types.KeyboardButton('Драмы')
        callback_button8 = types.KeyboardButton('Приключения')
        callback_button9 = types.KeyboardButton('Спорт')
        callback_button10 = types.KeyboardButton('Семейные')
        callback_button11 = types.KeyboardButton('Триллеры')
        callback_button12 = types.KeyboardButton('Ужасы')
        callback_button13 = types.KeyboardButton('Фантастика')
        callback_button14 = types.KeyboardButton('Фэнтези')
        callback_button15 = types.KeyboardButton('Детские')
        keyboard5.add(callback_button1, callback_button2, callback_button4, callback_button6, callback_button8,
                      callback_button9, callback_button10, callback_button11, callback_button15)
        keyboard5.add(callback_button12, callback_button13, callback_button14)
        keyboard5.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Выберите жанр: ', reply_markup=keyboard5)



    elif message.text == 'Боевики':
        film = janri('boeviki')
        bot.send_message(message.chat.id,  film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Детективы':
        film = janri('detektivy')
        bot.send_message(message.chat.id,  film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Комедии':
        film = janri('komedii')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Драмы':
        film = janri('dramy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Приключения':
        film = janri('priklyucheniya-filmy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Спорт':
        film = janri('sport-filmy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Семейные':
        film = janri('semeynye')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Триллеры':
        film = janri('trillery')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Ужасы':
        film = janri('uzhasy-filmy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Фантастика':
        film = janri('fantastika-filmy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Фэнтези':
        film = janri('fentezi-filmy')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)
    elif message.text == 'Детские':
        film = janri('detskie')
        bot.send_message(message.chat.id, film[0])
        bot.send_message(message.chat.id, film[1])
        keyboard6 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        callback_button16 = types.KeyboardButton('Да')
        callback_button17 = types.KeyboardButton('Нет')
        keyboard6.add(callback_button16, callback_button17)
        keyboard6.add(types.KeyboardButton('Вернуться⬅️'))
        bot.send_message(message.chat.id, 'Хотите добавить фильм в избранное?', reply_markup=keyboard6)

    elif message.text == 'Да':
        with open('text1.txt', 'a', encoding='UTF-8') as file:
            film = janri('detskie')
            print(film[0], film[1], file=file)

        bot.send_message(message.chat.id, 'Вы добавили фильм в избранное')

    elif message.text == 'Нет':
        pass



    if message.text == 'Случайный фильм🎲':
        f = open("text.txt", "w")
        f.write("cлучайный")
        f.close()

        chat_id = message.chat.id
        bot.send_message(chat_id, "Обрабатываю запрос...")

        db = sqlite3.connect('Triangle_Kino.db')
        cur = db.cursor()

        for rand in cur.execute(
                'SELECT * FROM Triangle_Kino WHERE ID IN (SELECT ID FROM Triangle_Kino ORDER BY RANDOM() LIMIT 1)'):
            print(rand)
            bot.send_message(message.chat.id, str(f'{rand[2]}{rand[4]}{rand[5]}'))

bot.polling (none_stop=True)
