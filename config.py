from vkbottle import BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from vkbottle.bot import Bot
from vkbottle import PhotoMessageUploader

labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

TOKEN = 'vk1.a.vB5pV_pGLIdZ6i0zQVvupbNceWJclD4-mS7Vi19vH_kSHbthwsxVX9d4CozGbPy-HwhDjWb__VHB1820AGJVWJC9bLbRhGkST_aM_6McE5Eh_ef5Vy1iLemVDWwvWctuC3psRJZJa3TabFXvgX3xEpb-RWF3YJVDLRN3yy2VPRPub-yAfST0UYEscP5rp20TFP4AqQX8-nSBI_AJyWzAAg'

URL ='https://script.google.com/macros/s/AKfycbzqjh8b2sH48A3zKzVRZ6v5RlhcgDXiPQP_N7XG2cAsrmGDf_f18u1jGoPV9sbCE0Wr/exec'

bot = Bot(token=TOKEN, state_dispenser=state_dispenser)
photo_up = PhotoMessageUploader(bot.api)
