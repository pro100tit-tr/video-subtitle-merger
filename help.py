from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Help(object):

    HELP_USER = "??"

    HELP_TEXT ="""<b>Yardım Menüsüne Hoş Geldiniz</b>

1.) Bir Video dosyası veya url gönderin.
2.) Bir altyazı dosyası gönderin (ass veya srt)
3.) İstediğiniz muxing türünü seçin!

Dosyaya özel isim vermek için url'yi | ile ayrılmış olarak gönderin.
<i>url|özel_adı.mp4</i>

<b>Not : </b><i>Hardmux'ta yalnızca ingilizce yazı tiplerinin desteklendiğini lütfen unutmayın, diğer komut dosyaları videoda boş bloklar olarak gösterilecektir!</i> 
<a href="https://github.com/tellybots/video-sub-merger">Repo URL</a>"""



    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
