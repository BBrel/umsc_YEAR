from vkbottle import BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from vkbottle.bot import Bot
from vkbottle import PhotoMessageUploader

labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

TOKEN = 'vk1.a.vB5pV_pGLIdZ6i0zQVvupbNceWJclD4-mS7Vi19vH_kSHbthwsxVX9d4CozGbPy-HwhDjWb__VHB1820AGJVWJC9bLbRhGkST_aM_6McE5Eh_ef5Vy1iLemVDWwvWctuC3psRJZJa3TabFXvgX3xEpb-RWF3YJVDLRN3yy2VPRPub-yAfST0UYEscP5rp20TFP4AqQX8-nSBI_AJyWzAAg'
data = ''
URL ='https://script.google.com/macros/s/AKfycbySUryXThgdj5PnkkqE3OW6VtM1ygVez7G4cuoh4jdQmCZb8fqIDNMKZcArpgZGfsZS/exec'

bot = Bot(token=TOKEN, state_dispenser=state_dispenser)
photo_up = PhotoMessageUploader(bot.api)
