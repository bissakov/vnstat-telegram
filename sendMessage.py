#!/usr/bin/python

import requests
import buildTable
import secrets #secrets.py with bot token and chat id variables

bot_token = secrets.token
bot_chatID = secrets.chatID
api_url = 'https://api.telegram.org/bot' + bot_token + '/'

def sendImage(msg, img):
    method = "sendPhoto"
    params = {'chat_id': bot_chatID, 'caption': msg, 'parse_mode': 'MarkdownV2'}
    files = {'photo': img}
    resp = requests.post(api_url + method, params, files=files)
    return resp

message = buildTable.message
sendImage(message, open('daily.png', 'rb'))