from pypromptpay import qr_code 
import qrcode
from Project import QR__file_dir
import os


def Make_QR_for_user_promptpay(user_id,amount):
    text_qr_data = qr_code("0909846075",one_time=True,money=amount)

    QR_img = qrcode.make(text_qr_data)

    path = os.path.join(QR__file_dir,'QR_For_{}_.jpg'.format(user_id))

    with open(path,'wb') as im:
        QR_img.save(im,'JPG')
        im.close()
    
    return path


import datetime, time
import json
import requests

# Calculate the offset taking into account daylight saving time
utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
kbankTime = datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()

def Make_QR_for_user_Kbank(user_id,amount):
    url = "https://APIPORTAL.kasikornbank.com:12002/pos/qr_request"

    headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Cache-Control": "no-cache"
        }

    payload = json.dumps({
            "partnerTxnUid": "PARTNERTEST0001",
            "partnerId": "PTR9393674",
            "partnerSecret": "86ffe329aaca413db3b7ffc48063d5fb",
            "requestDt": kbankTime,
            "merchantId": "KB111969052275",
            "terminalId": "term1",
            "qrType": "3",
            "txnAmount": amount,
            "txnCurrencyCode": "THB",
            "reference1": "INV001",
            "reference2": 'null',
            "reference3": 'null',
            "reference4": 'null'
        })

    a = requests.post(url,headers = headers,data = payload)
    text_qr_data = a.json['qrCode']

    QR_img = qrcode.make(text_qr_data)

    path = os.path.join(QR__file_dir,'QR_For_{}_.jpg'.format(user_id))

    with open(path,'wb') as im:
        QR_img.save(im,'JPG')
        im.close()
    
    return path


