from flask import Flask
import os

app = Flask(__name__)
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
QR__file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'QR_CODE')

from linebot import (
    LineBotApi, WebhookParser
)

from urllib.parse import urlparse
o = urlparse(request.base_url)
host = o.hostname
## app_url = host
app_url = "https://uncle-merchant.herokuapp.com"



# get channel_secret and channel_access_token from your environment variable
channel_secret = '4e884f99620d9fa1d728a83f3e2a6c8e'
channel_access_token = 'brEjhlrvM0K9byTI0dJM6+syPX/ykchnIeiUHg3dfuDo5WAbofHCIJ8mxVk83RWasMrQiLigwt1/YRG+CVOipwqMl//Zy1O7hl1m640lpFsiT4h6c5/XOQfunU1r9my8fS6zK9fXiSL+7Qj2Z6CregdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

from Project import route

    

