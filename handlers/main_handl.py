from vkbottle.bot import Message
import config
from keyboards import activate
from state import State
from handlers import email_handl


@config.labeler.message(state=State.ACTIVE)
async def active(message: Message):
    pass


@config.labeler.message(state=State.EMAIL)
async def get_by_email(message: Message):
    await email_handl.start(message)


@config.labeler.message(func=lambda x: x.text != '2023')
async def greetings(message: Message):

    await message.answer(
        message='Привет! Давай подведём итоги года вместе с Умскул. '
                'Скорее пиши 2023 или жми на кнопку ниже, чтобы я подготовил данные',
        keyboard=activate
    )
