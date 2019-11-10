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

i = 0
users = {}

class pipe():
    def __init__(self, timemax, user_id, tests):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
        self.num = 0
        self.tests = tests
        self.exam = "math"
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
#Основа===========================================================================================================================================
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
                        message="Выберите предмет: \n"
                                " 1. Математика\n"
                                " 2. Информатика", keyboard=keyboard_subj)
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
                    db.child('users').child(self.user_id).child("results").child('math').set(0)
                    self.status = 3
                    continue
                elif text == 'статистика':
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Ваша статистика по предметам: \n Математика: " + str(db.child('users').child(self.user_id).child("results").child('math').get().val()) +
                                "\nИнформатика: " + str(db.child('users').child(self.user_id).child("results").child('cscience').get().val()) )
                elif text == 'вверх вверх вниз вниз влево вправо влево вправо б а':
                    vk.messages.send( 
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        message="Писал код: Степан Ларионов\n"
                                "База данных и библиотеки: Богдан Ивакин\n"
                                "Веб-разработка: Игнат Марковский\n"
                                "Дизайн, DJ и бета-тест: Артём Журиков\n"
                                "Бессменный лидер и наставник: Иван Гуляев", keyboard=keyboard_standart)
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
                    self.exam = "math"
                    continue
                if text == '2':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Ваш выбор: Информатика", keyboard=keyboard_standart)
                    self.status = 0
                    self.exam = "cscience"
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
                    db.child('users').child(self.user_id).child("post").set(True)
                    continue
                elif text == 'нет':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Авто-рассылка отключена!", keyboard=keyboard_standart)
                    self.status = 0
                    db.child('users').child(self.user_id).child("post").set(False)
                    continue
# Тестирование ============================================================================================
            if self.status == 3:
                if text == 'да':
                    self.status = 4
                    vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                            message=base.get_test(self.exam,task[self.tests]))
                    continue
                elif text == 'нет':
                    vk.messages.send(
                                    user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                    message="Хорошо", keyboard = keyboard_standart)
                    self.status = 0
                    continue
# Тестирование2======================================================================================================
            if self.status == 4:
                if self.tests !=0:
                    if text == db.child(self.exam).child(task[self.tests]).child("ans").get().val():
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647),
                            message="Правильный ответ!")
                        self.num += 1
                        db.child('users').child(self.user_id).child("results").child(self.exam).set(self.num)
                        self.tests -= 1
                        vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                                message=base.get_test(self.exam,task[self.tests]))
                        continue
                    elif text == 'отмена тестирования':
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_standart,
                            message="Тестирование отменено.")
                        self.tests = 0
                        self.num = 0
                        db.child('users').child(self.user_id).child("results").child(self.exam).set(self.num)
                        self.status = 0
                        continue
                    else:
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647),
                            message="Неправильный ответ!")
                        self.tests -= 1
                        vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_answr,
                                message=base.get_test(self.exam, task[self.tests]))
                        continue
#=================================================================================================================================
                elif self.tests == 0:
                    if text == db.child(self.exam).child(task[self.tests]).child("ans").get().val():
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647),
                            message="Правильный ответ!")
                        self.num += 1
                        db.child('users').child(self.user_id).child("results").child(self.exam).set(self.num)
                        vk.messages.send(
                                    user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                    message="Тестирование окончено! Введите 'Статистика'", keyboard = keyboard_standart)
                        self.status = 0
                        continue
                    elif text == 'отмена тестирования':
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647), keyboard=keyboard_standart,
                            message="Тестирование отменено.")
                        self.tests = 0
                        self.num = 0
                        db.child('users').child(self.user_id).child("results").child(self.exam).set(self.num)
                        self.status = 0
                        continue
                    else:
                        vk.messages.send(
                            user_id=self.user_id, random_id = random.randint(1, 2147483647),
                            message="Неправильный ответ!")
                        vk.messages.send(
                                    user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                    message="Тестирование окончено! Введите 'Статистика'", keyboard = keyboard_standart)
                        self.status = 0
                        continue
                    

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            if (str(event.user_id) in base.get_users()) and (event.user_id not in users):
                print("1")
                users[event.user_id] = pipe(10, event.user_id, 0)
                if users[event.user_id].life != True:
                    users[event.user_id].life = True
                    threading.Thread(target=users[event.user_id].do, args = []).start()
                    users[event.user_id].q.put(event.text.lower())
                users[event.user_id].q.put(event.text.lower())
            else:
                if event.user_id not in users:
                    users[event.user_id] = pipe(10, event.user_id, 0)
                    name = vk.users.get(user_ids = event.user_id, name_case = 'nom')[0]['first_name']
                    last_name = vk.users.get(user_ids = event.user_id, name_case = 'nom')[0]['last_name']
                    data = {'name':name,'last_name':last_name, 'user_id':event.user_id}
                    db.child('users').child(event.user_id).set(data)
                if users[event.user_id].life != True:
                    users[event.user_id].life = True
                    threading.Thread(target=users[event.user_id].do, args = []).start()
                users[event.user_id].q.put(event.text.lower())
        except ConnectionError as e:
                print(str(e))
                users[event.user_id].life = True
                threading.Thread(target=users[event.user_id].do, args = []).start()