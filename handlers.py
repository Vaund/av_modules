""" handlers from lexan4ik"""
# хендлеры
from lexan4ik_clean import start, query_handler
from pablo import start, query_handler
# настройки
from lexan4ik_clean import dict_search_user, search_dict, key_keyb
# функции
from lexan4ik_clean import try_out, search, card, card_desc
from pablo import new_admin, check_admin, check_admin2, del_admin


#Хендлер отлова /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,"Добро пожаловать")
        dict_search_user[message.from_user.id] = {"dict":search_dict.copy(),"m":[]}
        key_keyb(message.from_user.id)
        print(dict_search_user)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id,)
    id = call.message.chat.id
    flag = call.data[0:1]
    data = call.data[1:]
    print(call.data)
    print(call)
    if flag == "k":
        search(call.from_user.id, message_id=call.message.message_id, k_user=data)

    if flag == 'c':
        a, b = data.split("@")

        dict_search_user[call.from_user.id]["dict"][mass_search[int(a)]] = dict_search_user[call.from_user.id]["m"][int(b)]
        if try_out(call.from_user.id, call.message.message_id):
            key_keyb(call.from_user.id, messsage_id=call.message.message_id)
    if flag == 'n':
        card_desc(call.from_user.id,num=int(data),msg_id=call.message.message_id)
