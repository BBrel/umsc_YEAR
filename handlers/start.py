from vkbottle.bot import Message
import config
import asyncio
from pic_gen import gen_pic
from vkbottle.http import AiohttpClient
import random
from state import State


@config.labeler.message(text='2023')
async def start(message: Message):
    try:
        await config.state_dispenser.set(message.peer_id, State.ACTIVE)
        await message.answer(
            message='Ищу информацию...'
        )
        await asyncio.sleep(random.randint(2, 4))
        http_client = AiohttpClient()
        request = await http_client.request_json(method='GET',
                                                 url=config.URL,
                                                 params={'user_vk': message.from_id})
        if request['result']:
            await message.answer(
                message='Анализирую нули и единицы, скоро обо всем тебе расскажу!'
            )

            for par in request['result'][0]['data']:
                await asyncio.sleep(2)
                await gen_pic(request['result'][0]['vk_id'], list(par.keys())[0], list(par.values())[0])

            await asyncio.sleep(2)
            await message.answer(
                attachment='photo249282206_457258152_5592de16f77bb1dc78'
            )
        else:
            await message.answer(
                message='Не нашел информцию :(\n'
                        'Обратись к своему персональному менеджеру или куратору (Картинки сгенерируются)'
            )
            request = {"vk_id": message.from_id, "data": [
                {'hw': random.randint(10, 200)},
                {'ball': random.randint(10, 100)},
                {'live': random.randint(100, 5000)},
                {'rec': random.randint(500, 2000)}
            ]}
            for par in request['data']:
                await asyncio.sleep(2)
                await gen_pic(request['vk_id'], list(par.keys())[0], list(par.values())[0])

            await asyncio.sleep(2)
            await message.answer(
                attachment='photo249282206_457258152_5592de16f77bb1dc78'
            )
    except:
        print('Случилась ошибка')
    finally:
        await config.state_dispenser.delete(message.peer_id)

