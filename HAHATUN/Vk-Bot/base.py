#=======================================Import====================================================
import pyrebase
from config import db_config, vk_token
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#=================================================================================================
#
#=========================================Tokens==================================================
vktoken = '12608dbd12d1a37e7dc4a19ff218849b5c123b431f2014fbec393e2e06b59a8baa623e225d5b53d8ddde1'
pyrebase_path = "edubot72-firebase-adminsdk-ga2lf-a12ce0d85e.json"
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
    firebase = pyrebase.initialize_app(db_config(pyrebase_path))
    auth = firebase.auth()
    db = firebase.database()
    return db


def get_user_info(id):
    info = db.child("users").child(id).get().val()
    return info


def get_test(exam, work): # Return task from exam
                 # Надо переделать структуру скорее всего, и подвести под адекватный вид
                          # Тут можно сразу словарём выдавать, смотри на get_user_info
    test = db.child(exam).child(work).get().val()
    outstr = test["que"] + "\n\na) " + test["1"] + "\nб) " + test["2"]+ "\nв) " + test["3"]+ "\nг) " + test["4"] + "\nОтвет?"
    return outstr

def get_users():
    users_id = db.child("users").get().val().keys()
    get_users = list(users_id)
    return get_users

def get_adm():
    adm_id = db.child("admins").get().val().keys()
    get_adm = list(adm_id)
    return get_adm

def get_results(exam):
    users_id = db.child("users").get().val().keys()
    data = []
    for users in users_id:
        result = db.child('users').child(users).child('results').child(exam).get().val()
        name = db.child('users').child(users).child('name').get().val()
        last_name = db.child('users').child(users).child('last_name').get().val()
        string = (str(last_name) + ' ' + str(name) + ' : ' + str(result))
        data.append(string)
    return data


db = init_db()


#================================================================================================