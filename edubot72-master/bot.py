#coding=<UTF-8>
import requests
# import pyrebase
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import base
import config
import threading
import queue
import re
import os
import test
from pprint import pprint


db = base.init_db()
vk = base.init_vk()
longpoll = base.init_longpoll()

keyboard_standart = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_standart.json"), "r", encoding="UTF-8").read()
keyboard_subj = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_subj.json"), "r", encoding="UTF-8").read()
keyboard_yn = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_yn.json"), "r", encoding="UTF-8").read()
keyboard_answr = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_answr.json"), "r", encoding="UTF-8").read()
keyboard_adm = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_adm.json"), "r", encoding="UTF-8").read()
keyboard_null = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_null.json"), "r", encoding="UTF-8").read()
keyboard_myclass = open(os.path.join(__file__.replace('bot.py','keyboards'),"keyboard_myclass.json"), "r", encoding="UTF-8").read()
tasks={'math':[task for task in db.Tasks.math.find()]
,'cscience':[task for task in db.Tasks.cscience.find()]}
random.shuffle(tasks['math'])
random.shuffle(tasks['cscience'])
users = {}
subj = {"math":"Математика", "cscience":"Информатика"}
class admpipe():
    def __init__(self, timemax, user_id:int):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
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
            if self.status == 0:
                if text == 'whoami':
                    test.send_message(vk,self.user_id,"Вы - Админ",keyboard_adm)
                    continue
                elif text == 'добавить учителя':
                    test.send_message(vk,self.user_id,"Чтобы добавить учителя отправьте ссылку на его страницу вк.",keyboard_null)
                    self.status = 1
                    continue
                elif text == 'удалить учителя':
                    test.send_message(vk,self.user_id,"Чтобы удалить учителя отправьте ссылку на его страницу вк.",keyboard_null)
                    self.status = 2
                    continue
            elif self.status == 1:
                if text == 'Назад':
                    test.send_message(vk, self.user_id, "Меню",keyboard_adm)
                    self.status=0
                    continue
                else:
                    try:
                        split_id = re.split(r"/", text)
                        adm_id = vk.utils.resolveScreenName(screen_name = str(split_id[3]))["object_id"]
                        name = vk.users.get(user_ids = adm_id, name_case = 'nom')[0]['first_name']
                        last_name = vk.users.get(user_ids = adm_id, name_case = 'nom')[0]['last_name']
                        data_adm = {'name':name,'last_name':last_name}
                        db.Users.Admins.insert_one({data_adm})
                        test.send_message(vk,self.user_id,"Админ добавлен!",keyboard_adm)
                        self.status = 0
                        continue
                    except IndexError:
                        test.send_message(vk,self.user_id,"Неверная ссылка",keyboard_adm)
                        self.status = 0
                        continue

            elif self.status == 2:
                if text == 'Назад':
                    test.send_message(vk, self.user_id, "Меню",keyboard_adm)
                    self.status=0
                    continue
                else:
                    try:
                        split_id = re.split(r"/", text)
                        adm_id = vk.utils.resolveScreenName(screen_name = str(split_id[3]))["object_id"]
                        name = vk.users.get(user_ids = adm_id, name_case = 'nom')[0]['first_name']
                        last_name = vk.users.get(user_ids = adm_id, name_case = 'nom')[0]['last_name']
                        adm=db.Users.Admins.find_one({'name':name,'last_name':last_name,'adm_id':adm_id})
                        db.Users.Admins.delete_one({'_id':adm['_id']})
                        vk.messages.send( 
                                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                        message="Админ удален!", keyboard=keyboard_adm)
                        self.status = 0
                        continue
                    except IndexError:
                        vk.messages.send( 
                                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                        message="Неверная ссылка", keyboard=keyboard_adm)
                        self.status = 0
                        continue
            


class teachpipe():
    def __init__(self, timemax, user_id:int):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
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
        if self.status==0:
            if text == "Мои классы":
                string='Список ваших групп\n'
                info=test.get_info('Teachers',self.user_id)
                for group in info['groups']:
                    string+=group + '\n'
                test.send_message(vk,self.user_id,string,keyboard_myclass)
                self.status=1
                continue
            elif text == 'Мои предметы':
                info=test.get_info('Teachers',self.user_id)
                if info['subject']:
                    string=''
                    for subj in info['subject']:
                        string+=subj+'\n'
                    test.send_message(vk,self.user_id,string,keyboard_adm)
                    continue
                else:
                    test.send_message(vk,self.user_id,'Вы не ведёте не один предмет. Обратитесь к завучу для добавления предметов',keyboard_adm)
                    continue
                
        elif self.status==1:


            

                


class pipe():
    def __init__(self, timemax, user_id:int, tests):
        self.q = queue.Queue()
        self.time = timemax
        self.life = True
        self.user_id = user_id
        self.status = 0
        self.num = 0
        self.tests = tests
        self.helptest=None
        self.exam = "none"
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
                if text == 'whoami':
                    test.send_message(vk,self.user_id,"Вы - Пользователь",keyboard_standart)
                    continue
                elif text == 'начать':
                    test.send_message(vk,self.user_id,message="Добро пожаловать в EduBot72! Напишите 'Помощь' для получения списка команд.",keyboard=keyboard_standart)
                    continue
                elif text == 'помощь':                 
                    test.send_message(vk,self.user_id,"Список команд: \n"
                                "Предмет - выбор предмета для тестирования. \n"
                                "Статистика - вывод вашей статистики по предметам. \n"
                                "Рассылка - включение и отключение автоматической рассылки. \n"
                                "Видео - видео-лекция для изучения материала по предмету. \n"
                                "Тестирование - начало тестирования. \n"
                                "Помощь - вывод списка команд.")
                    continue
                elif text == 'предмет':
                    test.send_message(vk,self.user_id,"Выберите предмет: \n"
                                " 1. Математика\n"
                                " 2. Информатика",keyboard_subj)
                    self.status = 1
                    continue
                elif text == 'рассылка':
                    test.send_message(vk,self.user_id,"Включить авто-рассылку? \n Да \n Нет",keyboard_yn)
                    self.status = 2
                    continue
                elif text == 'видео':
                    vk.messages.send(
                        user_id=self.user_id, random_id = random.randint(1, 2147483647),
                        attachment="video316289109_456239236")
                    continue
                elif text == 'тестирование':
                    if self.exam == "none":
                        test.send_message(vk,self.user_id,"Перед тестированием выберите предмет.")
                        continue
                    else:
                        test.send_message(vk,self.user_id,"Начать тестирование по предмету: "+ subj[self.exam] +"?\nДа/Нет",keyboard_yn)
                        self.status = 3
                        continue
                elif text == 'статистика':
                    test.send_message(vk,self.user_id,"Ваша статистика по предметам: \n Математика: " + str(db.Users.Users.find_one({'user_id':self.user_id})['results']['math']) +
                                "\nИнформатика: " + str(db.Users.Users.find_one({'user_id':self.user_id})['results']['cscience']))
                elif text == 'вверх вверх вниз вниз влево вправо влево вправо б а':
                    
                    test.send_message(vk,self.user_id,"Писал код: Степан Ларионов\n"
                                "База данных и библиотеки: Богдан Ивакин\n"
                                "Веб-разработка: Игнат Марковский\n"
                                "Дизайн, DJ и бета-тест: Артём Журиков\n"
                                "Бессменный лидер и наставник: Иван Гуляев",keyboard_standart)
                else:
                    
                    test.send_message(vk,self.user_id,"Писал код: Степан Ларионов\n"
                                "База данных и библиотеки: Богдан Ивакин\n"
                                "Веб-разработка: Игнат Марковский\n"
                                "Дизайн, DJ и бета-тест: Артём Журиков\n"
                                "Бессменный лидер и наставник: Иван Гуляев",keyboard_standart)
                    continue
# Предмет=================================================================================================
            if self.status == 1:
                if text == '1':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Ваш выбор: Математика", keyboard=keyboard_standart)
                    self.status = 0
                    self.exam = "math"
                    self.helptest=base.get_test(tasks[self.exam])
                    continue
                elif text == '2':
                    vk.messages.send(
                                user_id=self.user_id, random_id = random.randint(1, 2147483647),
                                message="Ваш выбор: Информатика", keyboard=keyboard_standart)
                    self.status = 0
                    self.exam = 'cscience'
                    self.helptest=base.get_test(tasks[self.exam])
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
                    test.send_message(vk,self.user_id,"Авто-рассылка включена!",keyboard_standart)
                    self.status = 0
                    db.Users.Users.update_one({'user_id':self.user_id},{'$set':{'post':True}})
                    continue
                elif text == 'нет':                  
                    test.send_message(vk,self.user_id,"Авто-рассылка отключена!",keyboard_standart)
                    self.status = 0
                    db.Users.Users.update_one({'user_id':self.user_id},{'$set':{'post':False}})
                    continue
# Тестирование ============================================================================================
            if self.status == 3:
                if text == 'да':
                    self.num = 0
                    user=db.Users.Users.find_one({'user_id':self.user_id})
                    try:
                        user['results'][self.exam]=0
                    except KeyError:
                        db.Users.Users.update_one({'user_id':self.user_id},{'$set':{'results':{'math':0,'cscience':0}}})
                    db.Users.Users.update_one({'user_id':self.user_id},{'$set':user})
                    self.status = 4
                    self.task=next(self.helptest)
                    try:
                        test.send_message(vk,self.user_id,self.task["que"] + "\n\na) " + self.task["1"] + "\nб) " + self.task["2"]+ "\nв) " +
                                self.task["3"]+ "\nг) " + self.task["4"] + "\nОтвет?",keyboard_answr)
                    except TypeError:
                        self.status=3
                        text='да'
                    continue
                elif text == 'нет':
                    test.send_message(vk,self.user_id,'Хорошо',keyboard_standart)
                    self.status = 0
                    continue
# Тестирование2======================================================================================================
            if self.status == 4:
                if self.tests !=0:
                    if text == self.task['ans'] :
                        test.send_message(vk,self.user_id,"Правильный ответ!")
                        self.num += 1
                        helpuser=db.Users.Users.find_one({'user_id':self.user_id})
                        helpuser['results'][self.exam]=self.num
                        db.Users.Users.update_one({'user_id':self.user_id},{'$set':helpuser})
                        self.task=next(self.helptest)
                        self.tests -= 1
                        try:
                            test.send_message(vk,self.user_id,self.task["que"] + "\n\na) " + self.task["1"] + "\nб) " + self.task["2"]+ "\nв) " +
                                self.task["3"]+ "\nг) " + self.task["4"] + "\nОтвет?",keyboard_answr)
                        except TypeError:
                            self.status=3
                            text='да'
                        continue
                    elif text == 'отмена тестирования':
                        test.send_message(vk,self.user_id,"Тестирование отменено.",keyboard_standart)
                        self.tests = 0
                        self.num = 0
                        helpuser=db.Users.Users.find_one({'user_id':self.user_id})
                        helpuser['results'][self.exam]=self.num
                        db.Users.Users.update_one({'user_id':self.user_id},{'$set':helpuser})
                        self.status = 0
                        continue
                    else:
                        
                        test.send_message(vk,self.user_id,"Неправильный ответ!")
                        self.tests -= 1
                        self.task=next(self.helptest)
                        try:
                            
                            test.send_message(vk,self.user_id,self.task["que"] + "\n\na) " + self.task["1"] + "\nб) " + self.task["2"]+ "\nв) " +
                                self.task["3"]+ "\nг) " + self.task["4"] + "\nОтвет?",keyboard_answr)
                        except TypeError:
                            self.status=3
                            text='да'
                        continue
#=================================================================================================================================
                elif self.tests == 0:
                    
                    if text == self.task['ans'] : 
                        
                        test.send_message(vk,self.user_id,"Правильный ответ!")
                        self.num += 1
                        
                        helpuser=db.Users.Users.find_one({'user_id':self.user_id})
                        helpuser['results'][self.exam]=self.num
                        db.Users.Users.update_one({'user_id':self.user_id},{'$set':helpuser})
                        
                        test.send_message(vk,self.user_id,"Тестирование окончено! Введите 'Статистика'",keyboard_standart)
                        random.shuffle(tasks['math'])
                        random.shuffle(tasks['cscience'])
                        self.helptest=base.get_test(tasks[self.exam])
                        self.status = 0
                        continue
                    elif text == 'отмена тестирования':
                        
                        test.send_message(vk,self.user_id,"Тестирование отменено.",keyboard_standart)
                        self.tests = 0
                        self.num = 0
                        
                        helpuser=db.Users.Users.find_one({'user_id':self.user_id})
                        helpuser['results'][self.exam]=self.num
                        db.Users.Users.update_one({'user_id':self.user_id},{'$set':helpuser})
                        self.status = 0
                        continue
                    else:
                        
                        test.send_message(vk,self.user_id,"Неправильный ответ!")
                        test.send_message(vk,self.user_id,"Тестирование окончено! Введите 'Статистика'",keyboard_standart)
                        random.shuffle(tasks['math'])
                        random.shuffle(tasks['cscience'])
                        self.helptest=base.get_test(tasks[self.exam])
                        self.status = 0
                        continue
                    

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            if (str(event.user_id) in base.get_adm()):
                if event.user_id not in users:
                    users[event.user_id] = admpipe(10, event.user_id)
                    name = vk.users.get(user_ids = event.user_id, name_case = 'nom')[0]['first_name']
                    last_name = vk.users.get(user_ids = event.user_id, name_case = 'nom')[0]['last_name']
                    data = {'name':name,'last_name':last_name, 'user_id':event.user_id}
                    # db.child('admins').child(event.user_id).set(data)
                    db.Users.Admins.insert_one(data)
                if users[event.user_id].life != True:
                    users[event.user_id].life = True
                    threading.Thread(target=users[event.user_id].do, args = []).start()
                users[event.user_id].q.put(event.text.lower())
            else:
                if (str(event.user_id) in base.get_users()) and (event.user_id not in users):
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
                        # db.child('users').child(event.user_id).set(data)
                        db.Users.Users.insert_one(data)
                    if users[event.user_id].life != True:
                        users[event.user_id].life = True
                        threading.Thread(target=users[event.user_id].do, args = []).start()
                    users[event.user_id].q.put(event.text.lower())
        except ConnectionError as e:
            print(str(e))
            users[event.user_id].life = True
            threading.Thread(target=users[event.user_id].do, args = []).start()