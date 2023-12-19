import random
from vkbottle.bot import Message
import config
import asyncio
from pic_gen import pics_loop
from state import State
from utilits import aio_request


async def start(message: Message, try_num=1):
    if try_num <= 3:
        try:
            request = await aio_request(config.URL, {'user': 'https://vk.com/id'+str(message.from_id)})

            if request['result']:
                await pics_loop(message, request['result'][0])

            else:
                await message.answer(
                    message='Не получилось найти тебя по ВК.\n'
                            'Напиши мне, с какой почтой ты зарегистрирован в Умскул'
                )
                await config.state_dispenser.set(message.peer_id, State.EMAIL)

        except Exception as exp:
            print(f'Случилась ошибка {exp}')
            await asyncio.sleep(random.uniform(1, 2))
            await start(message, try_num+1)
