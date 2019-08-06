from Project import app , static_file_dir ,line_bot_api
from flask import send_from_directory , abort , request , session , send_file , render_template

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,PostbackEvent,BaseSize , ImagemapAction , ImagemapSendMessage , ImagemapArea , MessageImagemapAction
)

from Project.Promptpay import Make_QR_for_user_Kbank,Make_QR_for_user_promptpay

import uuid

from Project import parser

@app.route('/')
def hello_world():
    return 'Hello, World!'

# host project image
@app.route('/PIC/<filename>')
def return_Pic(filename): 
    return send_from_directory(static_file_dir,filename)

@app.route('/PIC/ImageMap/<filename>')
def return_ImageMap(filename): 
    path = static_file_dir + '/ImageMap'
    return send_from_directory(path,filename)

@app.route("/access_bot")
def accessbot():
    botID = 'line://ti/p/@473snduo'
    return render_template('bot.html',bot = botID)

from Project.MessageTemplate.MessageTemp import *

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event,FollowEvent):

            actions = []
            actions.append(MessageImagemapAction(
                  text = 'PROMOTION',
                  area = ImagemapArea(
                      x = 2, y = 2, width = 1040, height = 346
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = 'COURSES',
                  area = ImagemapArea(
                      x = 2, y = 346, width = 1040, height = 346
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = 'ABOUT UNCLE',
                  area = ImagemapArea(
                      x = 0, y = 690, width = 1040, height = 346
                  )
            ))

            message = ImagemapSendMessage(
                
                # base_url = 'https://' + request.host + '/PIC/ImageMap.jpg', # prevent cache
                base_url = 'https://' + request.host + '/PIC/ImageMap',
                alt_text = 'MAP',
                base_size = BaseSize(height=1040, width=1040),
                actions = actions
            )
            line_bot_api.reply_message(event.reply_token, message)
            return 'OK'
        
        elif isinstance(event,PostbackEvent):
            # print(event.postback.data) get postback data from Event
            data = event.postback.data
            for key,value in all_course.items():
                if data == key:
                    message = SetMenuMessage_Object(value)
                    send_flex(event.reply_token,message)
                    return 'OK'


        elif isinstance(event,MessageEvent):
            if event.message.text == 'PROMOTION':
                message = SetMenuMessage_Object(course_02)
                send_flex(event.reply_token,message)
                return 'OK'
            
            elif event.message.text == 'COURSES':
                message = SetMenuMessage_Object(course_01)
                send_flex(event.reply_token,message)
                return 'OK'

        else :
            message = SetMenuMessage_Object(course_01)
            send_flex(event.reply_token , message)
            return 'OK'

    return 'OK'



