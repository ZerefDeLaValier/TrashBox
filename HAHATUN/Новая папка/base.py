import pyrebase
from config import db_config


def init_db():
    firebase = pyrebase.initialize_app(db_config("edubot72-firebase-adminsdk-ga2lf-a12ce0d85e.json"))
    auth = firebase.auth()
    db = firebase.database()
    return db


def get_user_info(id):
    info = db.child("users").child(id).get().val()
    return info


def get_test(exam, work): # Return task from exam
    test = {}             # Надо переделать структуру скорее всего, и подвести под адекватный вид
                          # Тут можно сразу словарём выдавать, смотри на get_user_info
    variants = db.child(exam).child(work).child("variants").get().val() + 1
    test['question'] = db.child(exam).child(work).child("que").get().val()
    for i in range(1,variants):
        test[str(i)] = db.child(exam).child(work).child(str(i)).get().val()
    test['answer'] = db.child(exam).child(work).child("ans").get().val()
    return test


db = init_db()

print(get_test("math","task1"))
