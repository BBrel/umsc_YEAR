import config
import asyncio
from pic_gen import gen_pic
from vkbottle.bot import Message


async def pics_loop(message: Message, request):
    await message.answer(
                    attachment='photo249282206_457258139_9f437581d2541b000c'
                )

    for par in request['data']:
        await asyncio.sleep(2)
        await gen_pic(
            vk_id=message.from_id,
            pic=list(par.keys())[0],
            dig=list(par.values())[0],
            ctx=message.ctx_api
        )

    await asyncio.sleep(2)
    await message.answer(
        attachment='photo249282206_457258152_5592de16f77bb1dc78'
    )
    await config.state_dispenser.delete(message.peer_id)
