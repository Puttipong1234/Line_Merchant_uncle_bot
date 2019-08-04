from flask import Flask, session , send_from_directory , request , session ,abort
import os

app = Flask(__name__)
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
QR__file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'QR_CODE')

from linebot import (
    LineBotApi, WebhookParser
)




from Project import route

# get channel_secret and channel_access_token from your environment variable
channel_secret = '77c6498f2b89f2df4959f8d21059559c'
channel_access_token = 'Lry+9veBfCmgtFB43jv8ir6wGqNgLw/rA6r89OA+cSAnjyKlighcNjZpwGG2VN0kB2xPn68RwzdiM17AKKPE4kW5OLWpBD+kO2LJ2NpPTZ/x0W5gsNocc1p4j5GL6KJ9tEDZjiPdjGPOz2x1ssawLwdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


    

