import requests
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import vk
i = 0
subj = 0

vk_session = vk_api.VkApi(token='12608dbd12d1a37e7dc4a19ff218849b5c123b431f2014fbec393e2e06b59a8baa623e225d5b53d8ddde1')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

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
        if event.text == 'Предмет' or event.text == 'предмет':
            i = 1
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                message="Выберите предмет: \n 1. Математика" )
        if event.text == 'Рассылка' or event.text == 'рассылка':
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Отключить авто-рассылку? \n Да \n Нет")
        if event.text == 'Статистика' or event.text == 'статистика':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Ваша статистика по предметам:")
        if event.text == 'Тестирование' or event.text == 'тестирование':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Начать тестирование? \n Да/Нет")
            i = 2
            
#------------------------------------------------------------------------------------------------------
        if i == 1:
            if event.text == "1":
                        vk.messages.send(
                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                            message="Матеша, я выбираю тебя!")
                        subj = 1
                        i = 0
        elif i == 2:
            if event.text == 'Да':
                vk.messages.send(
                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                            message="Тестирование начато!")
                i = 0
                if subj == 1:
                    print(6)
            elif event.text == 'Нет':
                vk.messages.send(
                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                            message="Ну и чмо же ты!")