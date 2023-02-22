# 20.02.23
# tg@vaund
import dotenv
import os

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread
import time

"""all lexan4ik's defs"""

from lexan import try_out, search, key_keyb, card, card_desc

"""all lexan4iks lists and dictionaries"""
from lists_and_dictionaries import mass_search
from lists_and_dictionaries import search_dict
from lists_and_dictionaries import dict_search_user
from lists_and_dictionaries import buf_auto
from lists_and_dictionaries import auto_

"""all pablo's defs"""
from pablo import check_admin2, new_admin, check_admin, del_admin

"""all pablos lists and dictionaries"""
from lists_and_dictionaries import dict_admins


"""main info(bot,gspread)"""
dotenv.load_dotenv(".env")

bot = telebot.TeleBot(os.environ["TOKEN"])
gc = gspread.service_account(os.environ["json_creds"])
sht2 = gc.open_by_url(os.environ["google_sheet"])
list_of_lists = sht2.worksheet("av_by").get_all_values()

"""pablo keyboards"""

from keyboards import inline_markup_main
from keyboards import inline_markup_n_admin
from keyboards import inline_markup_avto
from keyboards import inline_markup_del_admin
from keyboards import inline_markup_change_ad

"""lexan4ik handlers"""

def main():
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
        flag = call.data[0:2]
        data = call.data[2:]
        print(call.data)

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


    """pablo handlers"""


    @bot.message_handler(commands=['admin_start','newadmin','stat','newcar','help'])
    def start(message):
        if message.text == '/admin_start':
            bot.send_message(message.chat.id, "Проверка на администратора...")
            check_admin(message)

        if message.text == '/newadmin':
            if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
                bot.send_message(message.chat.id, "Перешлите сообщение и укажите уровень прав нового администратора")
            else:
                bot.send_message(message.chat.id, "У вас нет доступа")

        new_admin(message)

        if message.text == '/stat':
            if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
                bot.send_message(message.chat.id, "Вот вся статистика")
            else:
                bot.send_message(message.chat.id, "У вас нет доступа")

        if message.text == '/newcar':
            if message.chat.id in dict_admins:
                bot.send_message(message.chat.id, "Выберите действие с автомобилем", reply_markup=inline_markup_avto)
            else:
                bot.send_message(message.chat.id, "У вас нет доступа")

        if message.text == '/help':
            bot.send_message(message.chat.id, "Здесь должна быть помощь")


    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        bot.answer_callback_query(callback_query_id=call.id, )
        id = call.message.chat.id
        flag = call.data[0:2]
        data = call.data[2:]

        if flag == 'b0':
            bot.send_message(id, "Вы действительно хотите изменить администратора?", reply_markup=inline_markup_change_ad)

        if flag == 'o0':
            edit_a = bot.send_message(id, "Перешлите сообщение администратора, которого хотите изменить")
            bot.register_next_step_handler(edit_a, new_admin)

        if flag == 'p0':
            bot.send_message(id, "Отмена изменения")

        if flag == 'c0':
            bot.send_message(id, "Вы действительно хотите удалить администратора?", reply_markup=inline_markup_del_admin)

        if flag == 'j0':
            del_a = bot.send_message(id, "Перешлите сообщение администратора, которого хотите удалить")
            bot.register_next_step_handler(del_a, del_admin)

        if flag == 'l0':
            bot.send_message(id, "Отмена удаления")

        if flag == 'f0':
            dict_admins[forward_id] = {'user_name': forward_username, 'rights': ["False"]}
            bot.send_message(id, "Администратор добавлен")

            print(dict_admins)

        if flag == 'g0':
            dict_admins[forward_id] = {'user_name': forward_username, 'rights': ["True"]}
            bot.send_message(id, "Администратор добавлен")
            print(dict_admins)
    bot.infinity_polling()

if __name__ == "__main__":
    print("Bot ready")
    main()


