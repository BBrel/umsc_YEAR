from vkbottle.bot import Message
import config
import asyncio
from pic_gen import gen_pic
from vkbottle.http import AiohttpClient
from state import State
import json


@config.labeler.message(state=State.EMAIL)
async def start(message: Message):
    try:
        await config.state_dispenser.set(message.peer_id, State.ACTIVE)

        await message.answer(
            message='Ищу...'
        )

        http_client = AiohttpClient(json_processing_module=json)
        request = await http_client.request_json(method='GET',
                                                 url=config.URL,
                                                 params={'user_vk': message.from_id})

        if request['result']:
            await message.answer(
                attachment='photo249282206_457258139_9f437581d2541b000c'
            )

            for par in request['result'][0]['data']:
                await asyncio.sleep(2)
                await gen_pic(
                    vk_id=request['result'][0]['vk_id'],
                    pic=list(par.keys())[0],
                    dig=list(par.values())[0],
                    ctx=message.ctx_api
                )

            await asyncio.sleep(2)
            await message.answer(
                attachment='photo249282206_457258152_5592de16f77bb1dc78'
            )

        else:
            await message.answer(
                message='Не получилось найти тебя по ВК. '
                        'Напиши мне, с какой почтой ты зарегистрирован в Умскул'
            )

            await config.state_dispenser.set(message.peer_id, State.EMAIL)

    except Exception as exp:
        print(f'Случилась ошибка {exp}')

    finally:
        await config.state_dispenser.delete(message.peer_id)
