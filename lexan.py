import dotenv
import os

import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread

dotenv.load_dotenv(".env")

bot = telebot.TeleBot(os.environ["TOKEN"])
gc = gspread.service_account(os.environ["json_creds"])
sht2 = gc.open_by_url(os.environ["google_sheet"])
list_of_lists = sht2.worksheet("av_by").get_all_values()

mass_search = ['Марка', 'Год выпуска', 'Объем двигателя', 'Тип двигателя', 'Тип авто', 'Геолокация продавца']
search_dict = {'Марка': None, 'Год выпуска': None, 'Объем двигателя': None, 'Тип двигателя': None, 'Тип авто': None,
               'Геолокация продавца': None}
dict_search_user = {}
buf_auto = []

# Словарь
auto_ = {}
for el in list_of_lists[1:]:
    auto_[el[13]] = {}
    for i in range(0, 13):

        if list_of_lists[0][i] == 'Массив картинок':
            auto_[el[13]][list_of_lists[0][i]] = el[i].split(',')
        else:

            auto_[el[13]][list_of_lists[0][i]] = el[i]
    if el[8] and el[6]:
        for n in range(2, len(el)):
            price = el[8]
            decode_price = price.encode("ascii", "ignore")
            decode_price = decode_price.decode()
            auto_[el[13]]['Цена'] = decode_price.replace('.', '')

            mileage = el[6]
            decode_mileage = mileage.encode("ascii", "ignore")
            decode_mileage = decode_mileage.decode()
            auto_[el[13]]['Пробег'] = decode_mileage.replace('.', '')


def try_out(id_user, message_id):
    global buf_auto
    buf = []
    for k, v in auto_.items():
        flag = True
        for k1, v2 in dict_search_user[id_user]["dict"].items():
            if v2 == None:
                pass
            elif v2 in v[k1]:
                pass
            else:
                flag = False
        if flag:
            buf.append(v)
    if len(buf) <= 6:
        buf_auto = buf
        bot.delete_message(message_id=message_id, chat_id=id_user)
        card(id_user, buf)
        return False
    else:
        return True


def search(id_user, k_user, message_id=""):
    global buf_auto
    buf = []
    for k, v in auto_.items():
        flag = True
        for k1, v2 in dict_search_user[id_user]["dict"].items():
            if v2 == None:
                pass
            elif v2 in v[k1]:
                pass
            else:
                flag = False
        if flag:
            buf.append(v)
    if len(buf) <= 6:
        buf_auto = buf
        bot.delete_message(message_id=message_id, chat_id=id_user)
        card(id_user, buf)
        return False
    else:
        keyb = InlineKeyboardMarkup()

        ind = mass_search.index(k_user)
        text = f"выберите {k_user}"
        buf_var = []
        for car in buf:
            buf_var.append(car[k_user])

        buf_var = sorted(list(set(buf_var)))
        print(buf_var)
        for x in buf_var:
            keyb.add(InlineKeyboardButton(x, callback_data=f"c1{ind}@{buf_var.index(x)}"))

        dict_search_user[id_user]["m"] = buf_var
        if message_id == "":
            bot.send_message(id_user, text, reply_markup=keyb)
        if message_id != "":
            bot.edit_message_text(message_id=message_id, chat_id=id_user, text=text, reply_markup=keyb)


def key_keyb(id_user, messsage_id=""):
    keyb = InlineKeyboardMarkup()
    for k1, v2 in dict_search_user[id_user]["dict"].items():
        if v2 == None:
            keyb.add(InlineKeyboardButton(k1, callback_data=f"k1{k1}"))
    if messsage_id != "":
        bot.edit_message_text(chat_id=id_user, message_id=messsage_id, text="Выберите следующий критерий",
                              reply_markup=keyb)
    else:
        bot.send_message(id_user, "Выберите критерий", reply_markup=keyb)


def card(id_user, buf):
    for buffer in buf:
        keybb = InlineKeyboardMarkup()
        indx = buf.index(buffer)
        text = ''
        for a, b in buffer.items():
            if a != 'Массив картинок' and a != 'Описание' and a != 'Картинка':
                text += f'{a}: {b}\n'
            if a == 'Картинка':
                picture = b
        keybb.add(InlineKeyboardButton('Подробнее', callback_data=f'n1{str(indx)}'))
        bot.send_photo(id_user, picture, caption=text, reply_markup=keybb)


def card_desc(id_user, num, msg_id):
    text = ''
    picture = []
    picture_list = []
    for a, b in buf_auto[num].items():
        if a != 'Массив картинок' and a != 'Картинка':
            if a != 'Описание':
                text += f'{a}: {b}\n'
            else:
                text += f'\n{b}'
        elif a == 'Массив картинок':
            for pp in b:
                pp = pp.replace(' ', '')
                picture_list.append(pp)
        else:
            pass
    for pict in picture_list:
        picture.append(types.InputMediaPhoto(f'{pict}', caption=text[0:1024] if picture_list[0] == pict else None))
    bot.delete_message(chat_id=id_user, message_id=msg_id)
    bot.send_media_group(id_user, picture)


# Хендлер отлова /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, "Добро пожаловать")
        dict_search_user[message.from_user.id] = {"dict": search_dict.copy(), "m": []}
        key_keyb(message.from_user.id)
        print(dict_search_user)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    id = call.message.chat.id
    flag = call.data[0:1]
    data = call.data[1:]
    print(call.data)
    print(call)
    if flag == "k1":
        search(call.from_user.id, message_id=call.message.message_id, k_user=data)

    if flag == 'c1':
        a, b = data.split("@")

        dict_search_user[call.from_user.id]["dict"][mass_search[int(a)]] = dict_search_user[call.from_user.id]["m"][
            int(b)]
        if try_out(call.from_user.id, call.message.message_id):
            key_keyb(call.from_user.id, messsage_id=call.message.message_id)
    if flag == 'n1':
        card_desc(call.from_user.id, num=int(data), msg_id=call.message.message_id)


# print("Ready")
# bot.infinity_polling()
