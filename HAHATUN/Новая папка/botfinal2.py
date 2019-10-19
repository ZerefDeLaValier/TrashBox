import requests
import pyrebase
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json

task = ["task1","task2","task3","task4","task5","task6","task7","task8","task9","task10"]

config = {
  "apiKey": "AIzaSyCfS72UjYiXTMPzyPOU3zzphYKShw3d1XE",
  "authDomain": "edubot72.firebaseapp.com",
  "databaseURL": "https://edubot72.firebaseio.com",
  "storageBucket": "edubot72.appspot.com",
  "serviceAccount": "C:\TrashBox\HAHATUN\Bot\edubot72-firebase-adminsdk-ga2lf-a12ce0d85e.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

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
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == '1':
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Матеша, я выбираю тебя!")
                        break
        if event.text == 'Рассылка' or event.text == 'рассылка':
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Отключить авто-рассылку? \n Да \n Нет")
        if event.text == 'Статистика' or event.text == 'статистика':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Ваша статистика по предметам: \n Математика: " + str(num))
        if event.text == 'Тестирование' or event.text == 'тестирование':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                 message="Начать тестирование? \n Да/Нет")
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'Да':
                        num = 0
                        tests = 9
                        while tests != -1:
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message=db.child("math").child(task[tests]).child("que").get().val())
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message=db.child("math").child(task[tests]).child("1").get().val())
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message=db.child("math").child(task[tests]).child("2").get().val())
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message=db.child("math").child(task[tests]).child("3").get().val())
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message=db.child("math").child(task[tests]).child("4").get().val())
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message="Ответ?")
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                    if event.text == db.child("math").child(task[tests]).child("ans").get().val() :
                                        vk.messages.send(
                                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                            message="Правильный ответ!")
                                        num += 1
                                        break
                                    else:
                                        vk.messages.send(
                                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                            message="Неправильный ответ!")
                                        break
                            tests -= 1
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Тестирование окончено! Введите 'Статистика'")
                        break
                    elif event.text == 'Нет':
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Ну и чмо же ты!")
                        break
            