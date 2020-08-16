import random
import base

db = base.init_db()
def send_message(init,user_id,message,keyboard=None):
    if keyboard:
        init.messages.send(user_id=user_id,message=message,keyboard=keyboard,random_id=random.randrange(1,2147483647))
    else:
        init.messages.send(user_id=user_id,message=message,random_id=random.randrange(1,2147483647))


def get_collection(db,collection):
    return db.KCPT.collection.find()


def get_info(collection,user_id):
    return db.KCPT.collection.find_one({"user_id":int(user_id)})

