import requests
import pyrebase
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import base
import config

db = base.init_db()
vk = base.init_vk()
longpoll = base.init_longpoll()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Начать' or event.text == 'начать':
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                message="Добро пожаловать в EduBot72! Напишите 'Помощь' для получения списка команд." )
        if event.text == 'Помощь' or event.text == 'помощь': 
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Список команд: \n Предмет - выбор предмета для тестирования. \n Статистика - вывод вашей статистики по предметам. \n Рассылка - включение и отключение автоматической рассылки. \n Тестирование - начало тестирования. \n Помощь - вывод списка команд." )
        