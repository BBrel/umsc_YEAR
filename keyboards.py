from vkbottle import Keyboard, KeyboardButtonColor, Text

activate = (
    Keyboard(one_time=False, inline=True)
    .add(Text("2023"), KeyboardButtonColor.POSITIVE)
).get_json()
