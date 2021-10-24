from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class About(object):

    ABOUT_TEXT = """
**Bot :** 'Video Altyazı Birleşmesi'
**Yaratıcı :** Tellybots_4u
**Kredi :** 'Bu yolculuktaki herkes'
**Dil :** [Python3](https://python.org)
**Kütüphane :** [Pyrogram v1.2.0](https://pyrogram.org)
**Sunucu:** [Heroku](https://heroku.com) 
"""
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Ana Sayfa', callback_data='home'),
        InlineKeyboardButton('Kapat 🔐', callback_data='close')
        ]]
    )
