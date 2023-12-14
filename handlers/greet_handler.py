from vkbottle.bot import Message
import config
from keyboards import activate
from state import State


@config.labeler.message(state=State.ACTIVE)
async def active(message: Message):
    print('отработал актив')


@config.labeler.message(text=['Начать', 'начать', 'start', 'Start'])
async def greetings(message: Message):

    # greeting_photo = await config.photo_up.upload(
    #     file_source='photo249282206_457258139_9f437581d2541b000c',
    #     peer_id=message.peer_id,
    # )
    # print(greeting_photo)

    await message.answer(
        message='Добро пожаловать! Я готов поделиться с тобой '
                'твоими результатами за этот год! Пиши мне "2023" '
                'и я начну собирать информацию о твоих успехах!',
        keyboard=activate,
        attachment='photo249282206_457258139_9f437581d2541b000c'
    )


@config.labeler.message(func=lambda x: x.text != '2023')
async def text_handler(message: Message):

    await message.answer(
        message='Скорее пиши мне "2023"!',
        keyboard=activate
    )
