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
            request = await aio_request(config.URL, {'user': message.text})

            if request['result']:
                await pics_loop(message, request['result'][0])

            else:
                await message.answer(
                    message='Данная почта не найдена\n'
                            'Обратись к своему ПМ или куратору, чтобы тебе помогли'
                )
                await config.state_dispenser.delete(message.peer_id)

        except Exception as exp:
            print(f'Случилась ошибка {exp}')
            await asyncio.sleep(random.uniform(1, 2))
            await start(message, try_num+1)
