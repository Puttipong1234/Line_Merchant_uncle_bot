import datetime, time

# Calculate the offset taking into account daylight saving time
utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
kbankTime = datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()

from flask import Flask
import requests
import json


# Payload Example
# {
#     "url": "https://APIPORTAL.kasikornbank.com:12002/pos/qr_request",
#     "method": "POST",
#     "headers": {
#         "Content-Type": "application/json",
#         "Cache-Control": "no-cache"
#     },
#     "body": {
#         "partnerTxnUid": "PARTNERTEST0001",
#         "partnerId": "PTR4641985",
#         "partnerSecret": "e6ab2b80220f42989c6e9a5c36ad9c51",
#         "requestDt": kbankTime,
#         "merchantId": "KB111969052275",
#         "terminalId": "term1",
#         "qrType": "3",
#         "txnAmount": 100.5,
#         "txnCurrencyCode": "THB",
#         "reference1": "INV001",
#         "reference2": 'null',
#         "reference3": 'null',
#         "reference4": 'null',
#         "metadata": "ถุงผ้า 80.50, ดินสอ 20.00"
#     }
# }


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
        "txnAmount": 100.5,
        "txnCurrencyCode": "THB",
        "reference1": "INV001",
        "reference2": 'null',
        "reference3": 'null',
        "reference4": 'null',
        "metadata": "ถุงผ้า 80.50, ดินสอ 20.00"
    })


a = requests.post(url,headers = headers,data = payload)
print(a.text)
