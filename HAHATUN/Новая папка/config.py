import pyrebase


def db_config(tokenpath):
    return ({
        "apiKey": "AIzaSyCfS72UjYiXTMPzyPOU3zzphYKShw3d1XE",
        "authDomain": "edubot72.firebaseapp.com",
        "databaseURL": "https://edubot72.firebaseio.com",
        "storageBucket": "edubot72.appspot.com",
        "serviceAccount": tokenpath  # path to firebase token json
    })


def vk_token():
    return ('12608dbd12d1a37e7dc4a19ff218849b5c123b431f2014fbec393e2e06b59a8baa623e225d5b53d8ddde1')


