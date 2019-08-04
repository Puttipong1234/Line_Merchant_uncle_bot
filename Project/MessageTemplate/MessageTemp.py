from Project import static_file_dir
import os

{
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
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
            "text": "ซื้อคอสเรียน - 01",
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