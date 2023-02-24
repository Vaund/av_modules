import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread


bot = telebot.TeleBot('5983674316:AAGnC3fkS2ZcLUBJhBccmoEUiPrbWlgB-TE')

gc = gspread.service_account(filename="calm-vine-332204-924334d7332a.json")
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1qhAMkYQ11Q7dr_ImtpjnqtSwFDsOy1Deu1mE58nTEys/edit#gid=0')
worksheet = sht2.sheet1
list_of_lists = worksheet.get_all_values()


def dt(s):
    s = s[1:]
    return s


def fs(st):
    return st[0]


dict_admins = {}
dict_admins[760148226] = {'user_name': 'UITAAP', 'rights': True}
dict_admins[665909535] = {'user_name': 'lexan4ik', 'rights': True}

dict_car = {}
for el in list_of_lists[1:]:
    dict_car[el[13]] = {}
    for i in range(0, 13):
        if list_of_lists[0][i] == 'Массив картинок':
            dict_car[el[13]][list_of_lists[0][i]] = el[i].split(',')
        else:
            dict_car[el[13]][list_of_lists[0][i]] = el[i]
dict_car['103365747'] = {'Марка': 'NisСаня', 'Модель': 'Primera', 'Картинка': 'https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', 'Год выпуска': '1991г.', 'Обьем двигателя': ' 2.0л', 'Тип двигателя': ' дизель', 'Пробег': ' 331\u2009000км', 'Тип авто': 'седан, передний привод, другой', 'Цена': '3300р.', 'Геолокация продавца': 'Смолевичи, Минская обл.', 'Инф о двигателе VIN': 'VIN', 'Массив картинок': ['https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5019.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5029.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5014.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5034.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5009.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5024.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5039.jpg'], 'Описание ': 'Все недостатки указаны на фотоЗа время моего владения было сделано:Замена антифризаШлифовка головы Замена маслосьёмных колпачков(машина не дымит)Заменён к-т приводного ремняЗамена ремня грм ( замена на 322000)Замена штатных динамиков на более по подвеске ничего не гремит и не стучит Заменен аккумулятор (есть гарантия)Корректор фар и регулировка зеркал рабочее Все остальные вопросы по телефону Торг у капота Тех.осмотр до сентября 2023'}

key_mass = ['Марка', 'Модель', 'Картинка', 'Год выпуска', 'Обьем двигателя', 'Тип двигателя', 'Пробег', 'Тип авто',
             'Цена', 'Геолокация продавца', 'Инф о двигателе VIN', 'Массив картинок', 'Описание ', 'ID']

buf = dict.fromkeys(key_mass)

dict_create_car = {}

dict_change_car = {}

my_car = {"103365747": {'Марка': 'Nissan', 'Модель': 'Primera', 'Картинка': 'https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', 'Год выпуска': '1991г.', 'Обьем двигателя': ' 2.0л', 'Тип двигателя': ' дизель', 'Пробег': ' 331\u2009000км', 'Тип авто': 'седан, передний привод, другой', 'Цена': '3300р.', 'Геолокация продавца': 'Смолевичи, Минская обл.', 'Инф о двигателе VIN': 'VIN', 'Массив картинок': ['https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5019.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5029.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5014.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5034.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5009.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5024.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5039.jpg'], 'Описание ': 'Все недостатки указаны на фотоЗа время моего владения было сделано:Замена антифризаШлифовка головы Замена маслосьёмных колпачков(машина не дымит)Заменён к-т приводного ремняЗамена ремня грм ( замена на 322000)Замена штатных динамиков на более по подвеске ничего не гремит и не стучит Заменен аккумулятор (есть гарантия)Корректор фар и регулировка зеркал рабочее Все остальные вопросы по телефону Торг у капота Тех.осмотр до сентября 2023'}, "103365748": {'Марка': 'Тойота', 'Модель': 'Primera', 'Картинка': 'https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', 'Год выпуска': '1990г.', 'Обьем двигателя': ' 2.9л', 'Тип двигателя': ' дизель', 'Пробег': ' 331\u2009000км', 'Тип авто': 'седан, передний привод, другой', 'Цена': '3900р.', 'Геолокация продавца': 'Смолевичи, Минская обл.', 'Инф о двигателе VIN': 'VIN', 'Массив картинок': ['https://avcdn.av.by/advertmedium/0001/6570/5004.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5019.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5029.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5014.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5034.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5009.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5024.jpg', ' https://avcdn.av.by/advertmedium/0001/6570/5039.jpg'], 'Описание ': 'Все недостатки указаны на фотоЗа время моего владения было сделано:Замена антифризаШлифовка головы Замена маслосьёмных колпачков(машина не дымит)Заменён к-т приводного ремняЗамена ремня грм ( замена на 322000)Замена штатных динамиков на более по подвеске ничего не гремит и не стучит Заменен аккумулятор (есть гарантия)Корректор фар и регулировка зеркал рабочее Все остальные вопросы по телефону Торг у капота Тех.осмотр до сентября 2023'}}



def proverka_p(idp):
    if idp in dict_admins:
        return dict_admins[idp]['rights']


def proverka_m(idm):
    if idm in dict_car:
        return idm



keybb = InlineKeyboardMarkup()
keybb.add(InlineKeyboardButton('Изменить информацию об автомобиле', callback_data='em'))


inline_markup = InlineKeyboardMarkup()
inline_markup.add(InlineKeyboardButton('Изменить информацию об автомобиле', callback_data='em'))
inline_markup.add(InlineKeyboardButton("Добавить новый автомобиль", callback_data="ad"))


markup123 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Да")
button2 = types.KeyboardButton("Нет")
markup123.add(button1)
markup123.add(button2)


inline_markup2 = InlineKeyboardMarkup()
for x in my_car:
    inline_markup2.add(InlineKeyboardButton(x, callback_data="mc" + x))


key_mass.remove("ID")
inline_markup3 = InlineKeyboardMarkup()
for x in key_mass:
    inline_markup3.add(InlineKeyboardButton(x, callback_data="22" + x))



# def proverka(msg):




@bot.message_handler(content_types=['text'])
def start(message):
    id = message.chat.id
    if message.text == '/start':
        if proverka_p(id) is True:
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "Меню пользователя", reply_markup=keybb)
    if message.text == 'Да':
        dict_create_car[message.from_user.id] = buf.copy()
        create_car(message)
    if message.text == 'Нет' or message.text == "stop":
        if proverka_p(id) is True:
            bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "Меню пользователя", reply_markup=keybb)


def create_car(message):
    id_ = message.from_user.id
    text = message.text
    flag = True
    if text != "Да" and text != "Нет":
        flag = False
    for k, v in dict_create_car[id_].items():
        if v is None and flag:
            m = bot.send_message(id_, f"Введите {k}")
            bot.register_next_step_handler(m, create_car)
            break
        elif v is None and not flag:
            dict_create_car[id_][k] = text
            flag = True
    if text == "stop":
        for k, v in dict_create_car[id_].items():
            dict_create_car[id_][k] = None
        bot.send_message(message.chat.id, "Админ меню", reply_markup=inline_markup)

    print(dict_create_car[id_])


def change_car(message):
    id_ = message.from_user.id
    text = message.text
    if text != "stop" and text != "/start":
        for k, v in dict_change_car[id_].items():
            if k == dict_data[id_]:
                dict_change_car[id_][k] = text
        print(dict_change_car)
        bot.send_message(message.chat.id, "Выберите что ещё хотите изменить. Для завершения и возврата в главное меню введите stop", reply_markup=inline_markup3)


dict_data = {}
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    print(call.data)
    bot.answer_callback_query(callback_query_id=call.id,)
    id = call.message.chat.id
    flag = call.data[0:2]
    data = call.data[2:]
    if flag == "em":
        print(data)
        bot.send_message(id, "Выберите автомобиль", reply_markup=inline_markup2)
    if flag == "ad":
        print(data)
        bot.send_message(id, "Хотите добавить новый автомобиль?", reply_markup=markup123)
    if flag == "mc":
        dict_change_car[id] = my_car[data]
        print(dict_change_car)
        bot.send_message(id, "Выберите что хотите изменить, для завершения и возврата в главное меню введите stop", reply_markup=inline_markup3)
    if flag == "22":
        dict_data[id] = data
        print(dict_data)
        msg = bot.send_message(id, "Введите  " + data)
        bot.register_next_step_handler(msg, change_car)



# worksheet.update(f'A92:N92{}', )

print("Ready")
bot.infinity_polling()


"""

bot.send_message(IdOfMessage, text)
сообщение


photo1 = open("file", 'rb')
bot.send_photo(IdOfMessage, photo=photo1)
photo1.close()
фото

audio1 = open("file", 'rb')
bot.send_audio(IdOfMessage, audio1)
audio1.close()
аудио

stic1 = open("file", 'rb')
bot.send_sticker(IdOfMessage, stic1)
stic1.close()
стикер
"""