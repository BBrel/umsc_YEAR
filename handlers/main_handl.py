from vkbottle.bot import Message
import config
from keyboards import activate
from state import State
from handlers import by_email
from handlers import by_vk


@config.labeler.message(state=State.ACTIVE)
async def active(message: Message):
    pass


@config.labeler.message(state=State.EMAIL)
async def get_by_email(message: Message):
    await config.state_dispenser.set(message.peer_id, State.ACTIVE)

    await message.answer(
        message='Выполняю поиск по твоей почте!'
    )
    await by_email.start(message)
    await config.state_dispenser.delete(message.peer_id)


@config.labeler.message(text='2023')
async def get_by_vk(message: Message):
    await config.state_dispenser.set(message.peer_id, State.ACTIVE)

    await message.answer(
        message='Начинаю поиск!'
    )
    await by_vk.start(message)


@config.labeler.message(func=lambda x: x.text != '2023')
async def greetings(message: Message):

    await message.answer(
        message='Привет! Давай подведём итоги года вместе с Умскул. '
                'Скорее пиши 2023 или жми на кнопку ниже, чтобы я подготовил данные',
        keyboard=activate
    )
