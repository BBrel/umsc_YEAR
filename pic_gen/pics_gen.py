import asyncio

from vkbottle import PhotoMessageUploader
from PIL import Image, ImageDraw, ImageFont
import config
import os


async def gen_pic(vk_id, pic, dig, ctx, try_num=1):
    if try_num <= 2:

        try:
            uploader = PhotoMessageUploader(api=ctx)
            param = str(dig)
            path = 'pics/' + pic + await get_category(pic, dig) + '.png'

            with Image.open(path) as image:
                image.load()

            draw = ImageDraw.Draw(image)

            pic_width, pic_height = image.size

            block_y = 734 if pic in ('hw', 'live') else 754
            param_y = 80 if pic in ('hw', 'live') else 60

            font = ImageFont.truetype(
                font="CoFoGothicBold.ttf",
                size=169
            )

            param_width = draw.textlength(
                text=param,
                font=font
            ) + 70

            draw.rounded_rectangle(
                xy=(pic_width // 2 - param_width // 2, block_y,
                    pic_width // 2 + param_width // 2, block_y + 179),
                radius=10,
                fill='white',
                outline='black',
                width=2
            )

            draw.text(
                xy=(pic_width // 2, pic_height // 2 - param_y),
                text=param,
                font=font,
                anchor='ms',
                fill=(255, 24, 8)
            )

            image.save(str(vk_id) + pic + '.png')

            photo = await uploader.upload(
                file_source=str(vk_id) + pic + '.png',
                peer_id=vk_id,
            )

            await config.bot.api.messages.send(
                peer_id=vk_id,
                random_id=0,
                attachment=photo
            )
            await asyncio.sleep(1)
            os.remove(str(vk_id) + pic + '.png')
            image.close()

        except Exception as exp:
            print(exp)
            print('еще одна попытка')
            await gen_pic(vk_id, pic, dig, ctx, try_num+1)


async def get_category(pic, dig):
    if pic == 'hw':
        if dig > 100:
            return '_good'
        elif 40 <= dig >= 60:
            return '_med'
        else:
            return '_bad'
    elif pic == 'ball':
        if dig > 61:
            return '_good'
        elif 40 <= dig >= 60:
            return '_med'
        else:
            return '_bad'
    elif pic == 'rec':
        if dig > 100:
            return '_good'
        elif 40 <= dig >= 60:
            return '_med'
        else:
            return '_bad'
    elif pic == 'live':
        if dig > 100:
            return '_good'
        elif 40 <= dig >= 60:
            return '_med'
        else:
            return '_bad'
