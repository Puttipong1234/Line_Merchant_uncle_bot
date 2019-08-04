from Project import app , static_file_dir
from flask import send_from_directory
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
    # return send_from_directory(static_file_dir,filename)
    return static_file_dir


# @app.route("/callback", methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # parse webhook body
#     try:
#         events = parser.parse(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     # if event is MessageEvent and message is TextMessage, then echo text
#     for event in events:
#         if session['user'] is None:
#             pass
        

#         elif session['user'] = 'Buying':
#             pass

        
#         elif session['user'] = 'paid':
#             pass
    
#     return '200'



