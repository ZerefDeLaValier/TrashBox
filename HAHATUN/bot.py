import vk_api
import time
import random
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
 
token = "b1679d6797118b368c5330d73c94aa352ac65cf23ebc0849dfa1baf9dab3f52ee6c2b98a180b803b89727"
 
vk = vk_api.VkApi(token="b1679d6797118b368c5330d73c94aa352ac65cf23ebc0849dfa1baf9dab3f52ee6c2b98a180b803b89727")
 
vk._auth_token()


    
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "начать":
                vk.method("messages.send", {"peer_id": id, "message": "Добро пожаловать в EduBot72! Напишите 'Помощь' для получения списка команд. ", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "помощь":
                vk.method("messages.send", {"peer_id": id, "message": "Список команд: \n Предмет - выбор предмета для тестирования. \n Статистика - вывод вашей статистики по предметам. \n Рассылка - включение и отключение автоматической рассылки. \n Помощь - вывод списка команд.", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "саня":
                vk.method("messages.send", {"peer_id": id, "message": "Хуй соси!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "пока":
                vk.method("messages.send", {"peer_id": id, "message": "Пока! Возвращайся ещё!", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Этой команды я пока что не знаю, но может скоро узнаю!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
