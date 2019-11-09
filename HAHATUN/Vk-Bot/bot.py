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

id_list = []

task = ["task1","task2","task3","task4","task5","task6","task7","task8","task9","task10"]
db = base.init_db()
vk = base.init_vk()
longpoll = base.init_longpoll()

keyboard_standart = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_standart.json", "r", encoding="UTF-8").read()
keyboard_subj = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_subj.json", "r", encoding="UTF-8").read()
keyboard_yn = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_yn.json", "r", encoding="UTF-8").read()
keyboard_answr = open("C:\\TrashBox\\HAHATUN\\Vk-Bot\\keyboard_answr.json", "r", encoding="UTF-8").read()

i = 0
users = {}
class pipe():
    def __init__(self, timemax, user_id, tests):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
        self.tests = tests
        threading.Thread(target=self.do, args = []).start()
    def do(self):
        while True:
            try:
                text = self.q.get(block=True, timeout = self.time)
            except queue.Empty as e:
                print(str(e))
                self.life = False
                print("Dead")
                break

            if self.status == 0: #Тут начало
                self.tests = 9
                if text == 'ассинхрон':
                    for i in range(5):
                        vk.messages.send( 
                            user_id=self.user_id, random_id = random.randint(1, 2147483647),
                            message="#ССАГдеАссинхрон, #СпасибоАркадий, #ДайБогЧтобыРаботало", keyboard=keyboard_standart)
                    continue
                elif text == 'начать':
                    vk.messages.send( 
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Добро пожаловать в EduBot72! Напишите 'Помощь' для получения списка команд.", keyboard=keyboard_standart)
                    continue
                elif text == 'помощь':
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Список команд: \n Предмет - выбор предмета для тестирования. \n Статистика - вывод вашей статистики по предметам. \n Рассылка - включение и отключение автоматической рассылки. \n Видео - видео-лекция для изучения материала по предмету. \n Тестирование - начало тестирования. \n Помощь - вывод списка команд." )
                    continue
                elif text == 'предмет':
                    vk.messages.send( 
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Выберите предмет: \n 1. Математика", keyboard=keyboard_subj)
                    self.status = 1
                    continue
                elif text == 'рассылка':
                    vk.messages.send( 
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Включить авто-рассылку? \n Да \n Нет", keyboard=keyboard_yn)
                    self.status = 2
                    continue
                elif text == 'видео':
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        attachment="video316289109_456239236")
                    continue
                elif text == 'тестирование':
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Начать тестирование?\nДа/Нет", keyboard=keyboard_yn)
                    num = 0
                    self.status = 3
                    continue
                elif text == 'вверх вверх вниз вниз влево вправо влево вправо б а':
                    vk.messages.send( 
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Писал код: Степан Ларионов\nБаза данных и библиотеки: Богдан Ивакин\nВеб-разработка: Игнат Марковский\nДизайн, DJ и бета-тест: Артём Журиков\nБессменный лидер и наставник: Иван Гуляев", keyboard=keyboard_standart)
                else:
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Я не знаю такой команды", keyboard = keyboard_standart)
                    continue
# Предмет=================================================================================================
            if self.status == 1:
                if text == '1':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Ваш выбор: Математика", keyboard=keyboard_standart)
                    self.status = 0
                    continue
                elif text == 'назад':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Меню", keyboard=keyboard_standart)
                    self.status = 0
                    continue
# Рассылка ======================================================================================================
            if self.status == 2:
                if text == 'да':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Авто-рассылка включена!", keyboard=keyboard_standart)
                    self.status = 0
                    id_list.append(self.user_id)
                    continue
                elif text == 'нет':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Авто-рассылка отключена!", keyboard=keyboard_standart)
                    self.status = 0
                    if self.user_id in id_list:
                        id_list.remove(self.user_id)
                    continue
# Тестирование ============================================================================================
            if self.status == 3:
                if text == 'да':
                    self.status = 4
                    vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                            message=db.child("math").child(task[self.tests]).child("que").get().val()+ '\n\na)'+ db.child("math").child(task[self.tests]).child("1").get().val()+ '  б)'+ db.child("math").child(task[self.tests]).child("2").get().val()+ '  в)'+ db.child("math").child(task[self.tests]).child("3").get().val()+ '  г)'+ db.child("math").child(task[self.tests]).child("4").get().val()+ '\nОтвет?')
                    continue
                elif text == 'нет':
                    vk.messages.send(
                                    user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                    message="Хорошо", keyboard = keyboard_standart)
                    self.status = 0
                    continue
# Ответ======================================================================================================
            if self.status == 4:
                if text == db.child("math").child(task[self.tests]).child("ans").get().val():
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Правильный ответ!")
                    num += 1
                    self.tests -= 1
                    vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                            message=db.child("math").child(task[self.tests]).child("que").get().val()+ '\n\na)'+ db.child("math").child(task[self.tests]).child("1").get().val()+ '  б)'+ db.child("math").child(task[self.tests]).child("2").get().val()+ '  в)'+ db.child("math").child(task[self.tests]).child("3").get().val()+ '  г)'+ db.child("math").child(task[self.tests]).child("4").get().val()+ '\nОтвет?')
                    continue
                elif text == 'отмена тестирования':
                    self.tests = 0
                    num = 0
                    self.status = 0
                    continue
                else:
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Неправильный ответ!")
                    self.tests -= 1
                    vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                            message=db.child("math").child(task[self.tests]).child("que").get().val()+ '\n\na)'+ db.child("math").child(task[self.tests]).child("1").get().val()+ '  б)'+ db.child("math").child(task[self.tests]).child("2").get().val()+ '  в)'+ db.child("math").child(task[self.tests]).child("3").get().val()+ '  г)'+ db.child("math").child(task[self.tests]).child("4").get().val()+ '\nОтвет?')
                    continue
                

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            if event.user_id not in users:
                users[event.user_id] = pipe(10, event.user_id, 0)
            if users[event.user_id].life != True:
                users[event.user_id].life = True
                threading.Thread(target=users[event.user_id].do, args = []).start()
            users[event.user_id].q.put(event.text.lower())
            print(event)
            print(users)
        except ConnectionError as e:
                print(str(e))
                users[event.user_id].q.put(event.text.lower())






"""             
        elif event.text.lower() == 'статистика':
            vk.messages.send(
                user_id=event.user_id, random_id = random.randint(1, 2147483647),
                message="Ваша статистика по предметам: \n Математика: " + str(num))
        
                        num = 0
                        tests = 9
                        while tests != -1:
                            vk.messages.send(
                                user_id=event.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                                message=db.child("math").child(task[tests]).child("que").get().val()+ '\n\na)'+ db.child("math").child(task[tests]).child("1").get().val()+ '  б)'+ db.child("math").child(task[tests]).child("2").get().val()+ '  в)'+ db.child("math").child(task[tests]).child("3").get().val()+ '  г)'+ db.child("math").child(task[tests]).child("4").get().val()+ '\nОтвет?')
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                    
                            tests -= 1
                        vk.messages.send(
                                    user_id=event.user_id, random_id = random.randint(1, 2147483647),
                                    message="Тестирование окончено! Введите 'Статистика'", keyboard = keyboard_standart)
                        break"""