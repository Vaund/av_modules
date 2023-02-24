#  S Получение статистики (Id)
#  #Проверка прав, если S – Выдаем полную статистикуЕсли нет то по тем машинам которые связанны с этим id

# Канал
# пост – функция принимает Id Машины – постит
# # Добавляет ключ к машине
# Функция изменения поста в канале (Id машины)
# Из словаря достает Id сообщения

import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot('5913090241:AAFBe2-3XIuVmTD-vBVU-zUqkztWUfVpBto');

dict_admins = {}
dict_forward = {}

# словарь админов

def check_admin2():

    dict_admins[810809759] = {'user_name': 'pasha', 'rights': True}
    dict_admins[647012868] = {'user_name': 'UITAAP22', 'rights': False}
    # dict_admins[647012869] = {'user_name': 'UITAAP2342', 'rights': True}
    # dict_admins[1919192859] = {'user_name': 'masha', 'rights': True}

check_admin2()


inline_markup_main = InlineKeyboardMarkup()
inline_btn_11 = InlineKeyboardButton('Изменить администратора', callback_data='b0')
inline_btn_22 = InlineKeyboardButton('Удалить администратора', callback_data='c0')
inline_markup_main.add(inline_btn_11)
inline_markup_main.add(inline_btn_22)



inline_markup_n_admin = InlineKeyboardMarkup()
inline_btn_1 = InlineKeyboardButton('Администратор', callback_data='f0')
inline_btn_2 = InlineKeyboardButton('Супер администратор', callback_data='g0')
inline_markup_n_admin.add(inline_btn_1, inline_btn_2)



inline_markup_avto = InlineKeyboardMarkup()
inline_btn_add_car = InlineKeyboardButton('Добавить автомобиль', callback_data='h0')
inline_btn_change_car = InlineKeyboardButton('Изменить автомобиль', callback_data='i0')
inline_btn_del_car = InlineKeyboardButton('Удалить автомобиль', callback_data='u0')
inline_markup_avto.add(inline_btn_add_car)
inline_markup_avto.add(inline_btn_change_car)
inline_markup_avto.add(inline_btn_del_car)



inline_markup_del_admin = InlineKeyboardMarkup()
inline_btn_del_admin = InlineKeyboardButton('Удалить', callback_data='j0')
inline_btn_del_admin2 = InlineKeyboardButton('Отмена', callback_data='l0')
inline_markup_del_admin.add(inline_btn_del_admin, inline_btn_del_admin2)



inline_markup_change_ad = InlineKeyboardMarkup()
inline_btn_change_ad1 = InlineKeyboardButton('Изменить', callback_data='o0')
inline_btn_change_ad2 = InlineKeyboardButton('Отмена', callback_data='p0')
inline_markup_change_ad.add(inline_btn_change_ad1, inline_btn_change_ad2)



inline_markup_change_ad2 = InlineKeyboardMarkup()
def keyb_change_ad():
    for k, v in dict_admins.items():
        # print(v['user_name'])
        inline_markup_change_ad2.add(InlineKeyboardButton(v['user_name'], callback_data=f'o1{v}'))



inline_markup_change_admin = InlineKeyboardMarkup()
inline_btn_change_admin1 = InlineKeyboardButton('Изменить имя', callback_data='t0')
inline_btn_change_admin2 = InlineKeyboardButton('Изменить права', callback_data='y0')
inline_markup_change_admin.add(inline_btn_change_admin1, inline_btn_change_admin2)



@bot.message_handler(content_types=['text'])
def start(message):

    # print(message.text)
    # print(message.chat.id, message)
    # bot.send_message(message.chat.id, message.id)

    if message.text == '/start':
        bot.send_message(message.chat.id, "Проверка на администратора...")
        check_admin(message)
        keyb_change_ad()


    if message.text == '/newadmin':
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Перешлите сообщение и укажите уровень прав нового администратора")
    new_admin(message)


    if message.text == '/stat':
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Вот вся статистика")


    if message.text == '/newcar':
        if message.chat.id in dict_admins:
            bot.send_message(message.chat.id, "Выберите действие с автомобилем", reply_markup=inline_markup_avto)

    if message.text == '/help':
        bot.send_message(message.chat.id, "Здесь должна быть помощь")



# добваление и изменение администаторов
def new_admin(message):
    if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
        try:
            # global forward_id
            forward_id = message.forward_from.id

            # global forward_username
            forward_username = message.forward_from.username

            dict_forward[message.chat.id] = forward_id, forward_username
            # print(dict_forward)
            # print(dict_forward.values())

            # print(forward_id)
            # print(forward_username)

            bot.send_message(message.chat.id, "Укажите уровень прав", reply_markup=inline_markup_n_admin)
            # dict_admins[forward_id] = {'user_name': forward_username}

            # print(dict_admins[forward_id])
        except:
            pass




# проверка на админа
def check_admin(message):
    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Вы супер администратор", reply_markup=inline_markup_main)
    except:
        pass

    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == False:
            bot.send_message(message.chat.id, "Вы администратор")
    except:
        pass

    try:
        if message.chat.id not in dict_admins:
            bot.send_message(message.chat.id, "Вы не админостратор")
    except:
        pass


# def edit_ad(message):
#     forward_id = message.forward_from.id
#
#     # global forward_username
#     forward_username = message.forward_from.username
#
#     dict_forward[forward_id] = forward_username
#     # print(dict_forward)
#     bot.send_message(message.chat.id, "Укажите уровень прав", reply_markup=inline_markup_n_admin)



# удалание админов
def del_admin(message):
    forward_id = message.forward_from.id
    dict_admins.pop(forward_id)
    bot.send_message(message.chat.id, "Администратор удалён")
    print(dict_admins)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    id = call.message.chat.id
    flag = call.data[0:2]
    data = call.data[2:]
    # print(call.message)
    # print(call.message.forward_from_message_id)
    # print(id)
    # print(data)


    if flag == 'b0':
        bot.send_message(id, "Вы действительно хотите изменить администратора?", reply_markup=inline_markup_change_ad)


    if flag == 'o0':
        edit_a = bot.send_message(id, "Выберите администратора, которого хотите изменить", reply_markup=inline_markup_change_ad2)
        # bot.register_next_step_handler(edit_a, edit_ad)

        # bot.send_message(id, call.message.id)


    if flag == 'o1':
        # print(data)
        for v in dict_admins.values():
            bot.send_message(id, f"Имя пользователя: {v['user_name']} \nУровень прав: {v['rights']}", reply_markup=inline_markup_change_admin)



    if flag == 't0':
        bot.send_message(id, "Укажите новое имя")


    if flag == 'y0':
        bot.send_message(id, "Укажите права")


    if flag == 'p0':
        bot.send_message(id, "Отмена изменения")


    if flag == 'c0':
        # bot.send_message(id, call.message.id)
        bot.send_message(id, "Вы действительно хотите удалить администратора?", reply_markup=inline_markup_del_admin)


    if flag == 'j0':
        del_a = bot.send_message(id, "Перешлите сообщение администратора, которого хотите удалить")
        bot.register_next_step_handler(del_a, del_admin)


    if flag == 'l0':
        bot.send_message(id, "Отмена удаления")




    if flag == 'f0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': "False"}
        bot.send_message(id, "Администратор добавлен")
        # print(dict_admins[forward_id])
        # print(forward_id)
        print(dict_admins)
        dict_forward.popitem()
        # print(dict_forward)

    if flag == 'g0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': "True"}
        bot.send_message(id, "Супер администратор добавлен")
        print(dict_admins)
        dict_forward.popitem()
        # print(dict_forward)
        # print(forward_id)
    #     print(dict_admins[forward_id])
        # print(dict_admins)


print("Ready")
bot.infinity_polling()


