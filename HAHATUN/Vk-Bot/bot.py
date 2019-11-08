import requests
import pyrebase
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import base
import config
import threading
import queue



task = ["task1","task2","task3","task4","task5","task6","task7","task8","task9","task10"]
db = base.init_db()
vk = base.init_vk()
longpoll = base.init_longpoll()

keyboard_standart = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_standart.json", "r", encoding="UTF-8").read()
keyboard_subj = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_subj.json", "r", encoding="UTF-8").read()
keyboard_yn = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_yn.json", "r", encoding="UTF-8").read()
keyboard_answr = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_answr.json", "r", encoding="UTF-8").read()
num = 0
users = {}
class pipe():
    def __init__(self, timemax, user_id):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
        threading.Thread(target=self.do, args = []).start()
    def do(self):
        while True:
            try:
                value = self.q.get(block=True, timeout = self.time)
            except queue.Empty as e:
                print(str(e))
                self.life = False
                print("Dead")
                break

            if self.status == 0: #Тут начало
                if event.text.lower() == 'ассинхрон':
                    vk.messages.send( 
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="#ССАГдеАссинхрон, #СпасибоАркадий, #ДайБогЧтобыРаботало", keyboard=keyboard_standart)
                    continue
                elif event.text.lower() == 'начать':
                    vk.messages.send( 
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="Добро пожаловать в EduBot72! Напишите 'Помощь' для получения списка команд.", keyboard=keyboard_standart)
                    continue
                elif event.text.lower() == 'помощь':
                    vk.messages.send(
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="Список команд: \n Предмет - выбор предмета для тестирования. \n Статистика - вывод вашей статистики по предметам. \n Рассылка - включение и отключение автоматической рассылки. \n Видео - видео-лекция для изучения материала по предмету. \n Тестирование - начало тестирования. \n Помощь - вывод списка команд." )
                    continue
                elif event.text.lower() == 'предмет':
                    vk.messages.send( 
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="Выберите предмет: \n 1. Математика", keyboard=keyboard_subj)
                    self.status = 1
                    continue
                elif event.text.lower() == 'рассылка':
                    vk.messages.send( 
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="Отключить авто-рассылку? \n Да \n Нет", keyboard=keyboard_yn)
                elif event.text.lower() == 'видео':
                    vk.messages.send(
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        attachment="video316289109_456239236")
                    continue
                elif event.text.lower() == 'тестирование':
                    vk.messages.send(
                        user_id=event.user_id, random_id = random.randint(1, 2147483647),
                        message="Начать тестирование?\nДа/Нет", keyboard=keyboard_yn)
                        self.status = 3
                        continue
                else:
                    vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message="Я не знаю такой команды", keyboard = keyboard_standart)
                    continue
                
                    self.status = 2
                    continue
            if self.status == 1:
                if event.text.lower() == '1':
                    vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message="Ваш выбор: Математика", keyboard=keyboard_standart)
                    self.status = 0
                    continue
                elif event.text.lower() == 'назад':
                    vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                message="Меню", keyboard=keyboard_standart)
                    self.status = 0
                    continue
            if self.status == 2:
                if event.text.lower() == 'да':
                    vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Рассылка отключена!", keyboard=keyboard_standart)
                    self.status = 0
                    continue
                elif event.text.lower() == 'нет':
                    vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Рассылка включена!", keyboard=keyboard_standart)
                    self.status = 0
                    continue
            if self.status == 3:
                
                

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            if event.user_id not in users:
                users[event.user_id] = pipe(10, event.user_id)
            if users[event.user_id].life != True:
                users[event.user_id].life = True
                threading.Thread(target=users[event.user_id].do, args = []).start()
            users[event.user_id].q.put(event.user_id, event.text.lower())
            print(event)
            print(users)
        except ConnectionError as e:
                print(str(e))
                users[event.user_id].q.put(event.user_id, event.text.lower())






"""             
        elif event.text.lower() == 'статистика':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                message="Ваша статистика по предметам: \n Математика: " + str(num))
        elif event.text.lower() == 'вверх вверх вниз вниз влево вправо влево вправо б а':
            vk.messages.send( 
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                message="Писал код: Степан Ларионов\nБаза данных и библиотеки: Богдан Ивакин\nВеб-разработка: Игнат Марковский\nДизайн, DJ и бета-тест: Артём Журиков\nБессменный лидер и наставник: Иван Гуляев", keyboard=keyboard_standart)
        
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text.lower() == 'да':
                        num = 0
                        tests = 9
                        while tests != -1:
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                                message=db.child("math").child(task[tests]).child("que").get().val()+ '\n\na)'+ db.child("math").child(task[tests]).child("1").get().val()+ '  б)'+ db.child("math").child(task[tests]).child("2").get().val()+ '  в)'+ db.child("math").child(task[tests]).child("3").get().val()+ '  г)'+ db.child("math").child(task[tests]).child("4").get().val()+ '\nОтвет?')
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                    if event.text == db.child("math").child(task[tests]).child("ans").get().val() :
                                        vk.messages.send(
                                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                            message="Правильный ответ!")
                                        num += 1
                                        break
                                    elif event.text.lower() == 'отмена тестирования':
                                        tests = 0
                                        num = 0
                                        break
                                    else:
                                        vk.messages.send(
                                            user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                            message="Неправильный ответ!")
                                        break
                            tests -= 1
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Тестирование окончено! Введите 'Статистика'", keyboard = keyboard_standart)
                        break
                    elif event.text.lower() == 'нет':
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Ну и чмо же ты!", keyboard = keyboard_standart)
                        break """
            
            