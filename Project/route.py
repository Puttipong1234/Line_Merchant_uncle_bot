from Project import app , static_file_dir , WebhookParser ,parser
from flask import send_from_directory , abort , request
from Project import session

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage

)

from Project.Promptpay import Make_QR_for_user_Kbank,Make_QR_for_user_promptpay

@app.route('/')
def hello_world():
    return 'Hello, World!'

# host project image
@app.route('/PIC/<filename>')
def return_Pic(filename): 
    return send_from_directory(static_file_dir,filename)

from Project.MessageTemplate.MessageTemp import course_01,course_02, send_flex, SetMenuMessage_Object

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
        if session['user'] is None:
            if isinstance(event,FollowEvent):
                message = SetMenuMessage_Object(course_02)
                send_flex(message)
                return '200'
            
            else :
                message = SetMenuMessage_Object(course_01)
                send_flex(message)
                return '200'

        else :
            return '200'
        


    
    return '200'



