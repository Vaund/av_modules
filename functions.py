import json
import dotenv
import os
import telebot
import gspread


dotenv.load_dotenv(".env")

bot = telebot.TeleBot(os.environ["TOKEN"])
gc = gspread.service_account(os.environ["json_creds"])
sht2 = gc.open_by_url(os.environ["google_sheet"])
list_of_lists = sht2.worksheet("av_by").get_all_values()
dict_new_car = {'Марка': None, 'Год выпуска': None, 'Объем двигателя': None, 'Тип двигателя': None, 'Тип авто': None,
               'Геолокация продавца': None}
new_car_list = []
flag=None
def new_car(message):
    global flag
    id_ = message.from_user.id
    text = message.text
    flag = None
    if text != "" and text != "/new_car":
        flag = False
    for k, v in dict_new_car[id_].items():
        print(k, v)
        if v == None:
            if flag:
                m = bot.send_message(id_, f"Какая/Какой {k} у новой машины? Отправь")
                bot.register_next_step_handler(m, new_car)
                break
            elif v != "":
                dict_new_car[id_][k] = text
                flag = True
        if dict_new_car[id_]["Геолокация продавца"] != None:
            new_car_list.append(dict_new_car)
            with open('added_cars.json', 'w', encoding='utf-8') as f:
                json.dump(new_car_list, f, ensure_ascii=False, indent=4)
            f = open('added_cars.json', 'r', encoding='utf-8')
            d = json.loads(f.read())
            f.close()
            print(d)

    print(dict_new_car[id_])