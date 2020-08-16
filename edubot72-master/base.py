#=======================================Import====================================================
from config import db_config, vk_token
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
import pymongo
import random
#=================================================================================================
#
#=========================================Tokens==================================================
vktoken = '12608dbd12d1a37e7dc4a19ff218849b5c123b431f2014fbec393e2e06b59a8baa623e225d5b53d8ddde1'
mongo_path='mongodb+srv://Admin:Hallo120@testapp-cpatp.mongodb.net/test?retryWrites=true&w=majority'
#=================================================================================================
#
#====================================Vk initialization============================================
def init_vk():
    vk_session = vk_api.VkApi(token = vk_token(vktoken))
    vk = vk_session.get_api()
    return vk
def init_longpoll():
    vk_session = vk_api.VkApi(token = vk_token(vktoken))
    longpoll = VkLongPoll(vk_session)
    return longpoll
#=================================================================================================
#
#===========================================Data Base=============================================
def init_db():
    db=pymongo.MongoClient(mongo_path)
    return db


def get_user_info(ident):
    userdb=db.Users
    usercoll=userdb.Users
    # info = db.child("users").child(id).get().val()
    info=usercoll.find_one({'user_id':ident})
    return info


def get_test(tasks): 
    for task in tasks:
        if list(task.keys())[1]!='countTask':
            yield task[list(task.keys())[1]]

def get_users():
    return [user for user in db.Users.Users.find()]

def get_adm():
    return [admin for admin in db.Users.Admins.find()]

def get_results(exam):
    data = []
    for user in get_users():
        result = user[list(user.keys())[1]]['results'][exam]
        name = user[list(user.keys())[1]]['name']
        last_name = user[list(user.keys())[1]]['last_name']
        string = (last_name + ' ' + name + ' : ' + str(result))
        data.append(string)
    return data


db = init_db()



#================================================================================================