import pyrebase


def db_config(tokenpath):
    return ({
        "apiKey": "AIzaSyCfS72UjYiXTMPzyPOU3zzphYKShw3d1XE",
        "authDomain": "edubot72.firebaseapp.com",
        "databaseURL": "https://edubot72.firebaseio.com",
        "storageBucket": "edubot72.appspot.com",
        "serviceAccount": tokenpath  # path to firebase token json
    })


def vk_token(token):
    return (token)


