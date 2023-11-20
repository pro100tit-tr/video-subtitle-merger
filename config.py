
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '13772818')
    APP_ID = os.environ.get('APP_ID', 'f7380f4f6952680a726af3334b1deb87
')
    API_HASH = os.environ.get('API_HASH', '6526053489:AAFJ2RsRK6KIBSJOfXgu7usAbCkzOCtjl9s')

    #comma seperated user id of users who are allowed to use
    #ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
