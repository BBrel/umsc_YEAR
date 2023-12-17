import random
from vkbottle.bot import Message
import config
import asyncio
from pic_gen import pics_loop
from vkbottle.http import AiohttpClient
from state import State
import json


@config.labeler.message(text='2023')
async def start(message: Message, try_num=1):
    if try_num <= 3:
        try:
            await config.state_dispenser.set(
                peer_id=message.peer_id,
                state=State.ACTIVE
            )

            await message.answer(
                message='Ищу...'
            )

            http_client = AiohttpClient(json_processing_module=json)
            request = await http_client.request_json(
                method='GET',
                url=config.URL,
                params={'user_vk': message.from_id}
            )

            if request['result']:
                await pics_loop(message, request['result'][0])

            else:
                await message.answer(
                    message='Не получилось найти тебя по ВК.\n'
                            'Напиши мне, с какой почтой ты зарегистрирован в Умскул'
                )

                await config.state_dispenser.set(
                    peer_id=message.peer_id,
                    state=State.EMAIL
                )

        except Exception as exp:
            print(f'Случилась ошибка {exp}')
            await asyncio.sleep(random.uniform(1, 2))
            await start(message, try_num+1)
