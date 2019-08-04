from Project import app_url , channel_access_token
import os
import json
import requests


def send_flex(reply_token,file_data):
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}

    file_data['replyToken'] = reply_token
    #### dumps file จาก dict ให้เป็น json
    file_data = json.dumps(file_data)
    r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    return '200'


def SetMenuMessage_Object(Message_data,Quick_Reply = False):
    file_data = {"replyToken":'', "messages": []}
    data = file_data['messages'].append(Message_data)
    return file_data



# all course template
course_01 = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": app_url +"/PIC/01.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "คอสเรียน Python",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "Rassberrypine",
              "margin": "none",
              "size": "xl",
              "align": "center",
              "gravity": "top",
              "weight": "bold",
              "color": "#007F4E"
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคานักศึกษา",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "2500 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคาบุลคลทั่วไป",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "5000 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคากลุ่ม",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "สามารถต่อรองได้",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "none",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                      "margin": "xxl"
                    },
                    {
                      "type": "text",
                      "text": "จำนวนที่นั่งเหลือ",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "1",
                      "flex": 10,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "/",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "30",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "none",
          "margin": "none",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "ซื้อคอสเรียน",

                "data": "RPINE"
              },
              "color": "#007F4E",
              "margin": "none",
              "height": "md",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ข้อมูลเพิ่มเติม",
                "uri": "http://uncle-engineer.com/"
              }
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": app_url +"/PIC/02.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "คอสเรียน Python",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "Django Web",
              "margin": "none",
              "size": "xl",
              "align": "center",
              "gravity": "top",
              "weight": "bold",
              "color": "#C50020"
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคานักศึกษา",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "3000 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคาบุลคลทั่วไป",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "6000 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคากลุ่ม",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "สามารถต่อรองได้",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "none",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                      "margin": "xxl"
                    },
                    {
                      "type": "text",
                      "text": "จำนวนที่นั่งเหลือ",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "1",
                      "flex": 10,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "/",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "30",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "none",
          "margin": "none",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "ซื้อคอสเรียน",

                "data": "DJANGO"
              },
              "color": "#C50020",
              "margin": "none",
              "height": "md",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ข้อมูลเพิ่มเติม",
                "uri": "http://uncle-engineer.com/"
              }
            }
          ]
        }
      },},
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": app_url +"/PIC/03.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "คอสเรียน Python",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "AUTOMATE BOT",
              "margin": "none",
              "size": "xl",
              "align": "center",
              "gravity": "top",
              "weight": "bold",
              "color": "#B400A4"
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคานักศึกษา",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "2500 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคาบุลคลทั่วไป",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "5500 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคากลุ่ม",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "สามารถต่อรองได้",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "none",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                      "margin": "xxl"
                    },
                    {
                      "type": "text",
                      "text": "จำนวนที่นั่งเหลือ",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "1",
                      "flex": 10,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "/",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "30",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "none",
          "margin": "none",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "ซื้อคอสเรียน",

                "data": "AUBOT"
              },
              "color": "#B400A4",
              "margin": "none",
              "height": "md",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ข้อมูลเพิ่มเติม",
                "uri": "http://uncle-engineer.com/"
              }
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": app_url +"/PIC/04.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "คอสเรียน Python",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "LINE CHATBOT",
              "margin": "none",
              "size": "xl",
              "align": "center",
              "gravity": "top",
              "weight": "bold",
              "color": "#006B83"
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคานักศึกษา",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "3000 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคาบุลคลทั่วไป",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "6000 บาท/ท่าน",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                    },
                    {
                      "type": "text",
                      "text": "ราคากลุ่ม",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "สามารถต่อรองได้",
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "none",
                  "margin": "xxl",
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                      "margin": "xxl"
                    },
                    {
                      "type": "text",
                      "text": "จำนวนที่นั่งเหลือ",
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold"
                    },
                    {
                      "type": "text",
                      "text": "5",
                      "flex": 10,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "/",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    },
                    {
                      "type": "text",
                      "text": "30",
                      "flex": 0,
                      "size": "sm",
                      "align": "end",
                      "color": "#AAAAAA"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "none",
          "margin": "none",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "postback",
                "label": "ซื้อคอสเรียน",

                "data": "LINEBOT"
              },
              "color": "#006B83",
              "margin": "none",
              "height": "md",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ข้อมูลเพิ่มเติม",
                "uri": "http://uncle-engineer.com/"
              }
            }
          ]
        }
      }
    ]
  }
}
# promotion template
course_02 =  {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "spacing": "md",
      "contents": [
        {
          "type": "text",
          "text": "PROMOTION",
          "margin": "none",
          "size": "xxl",
          "align": "center",
          "weight": "bold",
          "color": "#879610"
        },
        {
          "type": "text",
          "text": "ประจำเดือนนี้",
          "margin": "none",
          "size": "xl",
          "align": "center",
          "gravity": "center",
          "weight": "regular",
          "color": "#879610"
        },
        {
          "type": "separator",
          "margin": "md",
          "color": "#565656"
        },
        {
          "type": "image",
          "url": "https://uncle-merchant.herokuapp.com/PIC/01.jpg",
          "size": "full"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ลงทะเบียน ตอนนี้",
            "data": "RPINE"
          },
          "color": "#1B9000",
          "style": "primary"
        },
        {
          "type": "separator",
          "margin": "md",
          "color": "#565656"
        },
        {
          "type": "image",
          "url": "https://uncle-merchant.herokuapp.com/PIC/02.jpg",
          "size": "full"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ลงทะเบียน ตอนนี้",
            "data": "DJANGO"
          },
          "color": "#C50020",
          "style": "primary"
        }
      ]
    }
  }
}

### course template rasberrypine
RPINE = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": "https://edb51a3a.ngrok.io/PIC/01.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "xxl",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "คอสเรียน Python",
          "size": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "Rassberrypine",
          "margin": "none",
          "size": "xl",
          "align": "center",
          "gravity": "top",
          "weight": "bold",
          "color": "#007F4E"
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคานักศึกษา",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "2500 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคาบุลคลทั่วไป",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "5000 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคากลุ่ม",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "สามารถต่อรองได้",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "none",
              "margin": "xxl",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                  "margin": "xxl"
                },
                {
                  "type": "text",
                  "text": "จำนวนที่นั่งเหลือ",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "1",
                  "flex": 10,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "/",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "30",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "none",
      "margin": "none",
      "contents": [
        {
          "type": "spacer",
          "size": "xxl"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ซื้อคอสเรียน",
            "data": "RPINE"
          },
          "color": "#007F4E",
          "margin": "none",
          "height": "md",
          "style": "primary"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "ข้อมูลเพิ่มเติม",
            "uri": "http://uncle-engineer.com/"
          }
        }
      ]
    }
  }
}
### course template django
DJANGO = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://edb51a3a.ngrok.io/PIC/02.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "xxl",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "คอสเรียน Python",
          "size": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "Django Web",
          "margin": "none",
          "size": "xl",
          "align": "center",
          "gravity": "top",
          "weight": "bold",
          "color": "#C50020"
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคานักศึกษา",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "3000 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคาบุลคลทั่วไป",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "6000 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคากลุ่ม",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "สามารถต่อรองได้",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "none",
              "margin": "xxl",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                  "margin": "xxl"
                },
                {
                  "type": "text",
                  "text": "จำนวนที่นั่งเหลือ",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "1",
                  "flex": 10,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "/",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "30",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "none",
      "margin": "none",
      "contents": [
        {
          "type": "spacer",
          "size": "xxl"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ซื้อคอสเรียน",
            "data": "DJANGO"
          },
          "color": "#C50020",
          "margin": "none",
          "height": "md",
          "style": "primary"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "ข้อมูลเพิ่มเติม",
            "uri": "http://uncle-engineer.com/"
          }
        }
      ]
    }
  }
}
### course template aubot
AUBOT = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://edb51a3a.ngrok.io/PIC/03.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "xxl",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "คอสเรียน Python",
          "size": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "AUTOMATE BOT",
          "margin": "none",
          "size": "xl",
          "align": "center",
          "gravity": "top",
          "weight": "bold",
          "color": "#B400A4"
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคานักศึกษา",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "2500 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคาบุลคลทั่วไป",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "5500 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคากลุ่ม",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "สามารถต่อรองได้",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "none",
              "margin": "xxl",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                  "margin": "xxl"
                },
                {
                  "type": "text",
                  "text": "จำนวนที่นั่งเหลือ",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "1",
                  "flex": 10,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "/",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "30",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "none",
      "margin": "none",
      "contents": [
        {
          "type": "spacer",
          "size": "xxl"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ซื้อคอสเรียน",
            "data": "AUBOT"
          },
          "color": "#B400A4",
          "margin": "none",
          "height": "md",
          "style": "primary"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "ข้อมูลเพิ่มเติม",
            "uri": "http://uncle-engineer.com/"
          }
        }
      ]
    }
  }
}
### course template line
LINE = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://edb51a3a.ngrok.io/PIC/04.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "xxl",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "คอสเรียน Python",
          "size": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "LINE CHATBOT",
          "margin": "none",
          "size": "xl",
          "align": "center",
          "gravity": "top",
          "weight": "bold",
          "color": "#006B83"
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคานักศึกษา",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "3000 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคาบุลคลทั่วไป",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "6000 บาท/ท่าน",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_4-512.png"
                },
                {
                  "type": "text",
                  "text": "ราคากลุ่ม",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "สามารถต่อรองได้",
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "none",
              "margin": "xxl",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/png/512/131/131569.png",
                  "margin": "xxl"
                },
                {
                  "type": "text",
                  "text": "จำนวนที่นั่งเหลือ",
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "5",
                  "flex": 10,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "/",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                },
                {
                  "type": "text",
                  "text": "30",
                  "flex": 0,
                  "size": "sm",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "none",
      "margin": "none",
      "contents": [
        {
          "type": "spacer",
          "size": "xxl"
        },
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "ซื้อคอสเรียน",
            "data": "LINE"
          },
          "color": "#006B83",
          "margin": "none",
          "height": "md",
          "style": "primary"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "ข้อมูลเพิ่มเติม",
            "uri": "http://uncle-engineer.com/"
          }
        }
      ]
    }
  }
}

all_course = [RPINE,DJANGO,AUBOT,LINE]