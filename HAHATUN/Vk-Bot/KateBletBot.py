import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

vktoken = '19a6639ea6a31e7258b34272426298272531152a5c42a84a89e74fdbc1a7932c4e10ebf17f0048de7f317'
vk_session = vk_api.VkApi(token = vktoken)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text.lower() == 'начать':
            vk.messages.send(user_id=event.user_id, random_id = random.randint(1, 2147483647),message="Hello world")