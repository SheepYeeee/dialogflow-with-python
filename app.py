import json
from flask import Flask, request, abort,make_response,jsonify
from linebot import LineBotApi, WebhookHandler
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import pymysql
import re
from weather_lib import *



app= Flask(__name__)
line_bot_api = LineBotApi('xi3ziO6Yv6J2b4nz1vSLMMIRRTehz9VFkWpgzytaDNpKxhdnRbcGWzORpjZGUJd8cJ4StMvKZ4lYtn9ZYEi80ckyu0hcjdtq9+hFttTk/ztv0uKckGTaOGjbiCuxvY0zDJClw0Hf7Dj1ek11lsb6RgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a8acf3539e24e1b315f7be19ae0000bf')

# ngrok authtoken 7opmFdz4EXQnKC95w7Pvo_6XusjhM3F7Rwv66GFrvUr

@app.route('/')
def hello():
    return 'trivago'

@app.route('/callback',methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResult(req):

    if req.get('queryResult').get('action') != "askweather":
        print("Please check your action name in DialogFlow...")
        return {}

    result = req.get("queryResult")
    parameters = result.get("parameters")
    citys = parameters.get('taiwan-city')
    city = "".join(citys)
    if city == "taichung":
        a = Taichung_City()
        b ='\n'.join(a)
        speech = b
    elif city == "taipei":
        a = Taipei_City()
        b ='\n'.join(a)
        speech = b
    elif city == "tainan":
        a = Tainan_City()
        b ='\n'.join(a)
        speech = b
    elif city == "kaohsiung":
        a = Kaohsiung_City()
        b ='\n'.join(a)
        speech = b
    elif city == "桃園":
        a = Taoyuan_City()
        b ='\n'.join(a)
        speech = b
    else:
        speech = "Hi," + city 
    print("Response:"+speech)
    my_result = {
                    "fulfillmentText": speech,
                    "source": "agent"
                }
    return my_result

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if  "台中天氣" in event.message.text or "臺中天氣" in event.message.text:
        a = Taichung_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "台北天氣" in event.message.text or "臺北天氣" in event.message.text:
        a = Taipei_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "桃園天氣" in event.message.text:
        a = Taoyuan_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "新竹天氣" in event.message.text:
        a = Hsinchu_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "台南天氣" in event.message.text or "臺南天氣" in event.message.text:
        a = Tainan_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "高雄天氣" in event.message.text:
        a = Kaohsiung_City()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "台東天氣" in event.message.text or "臺東天氣" in event.message.text:
        a = Taitung_County()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "花蓮天氣" in event.message.text:
        a = Hualien_County()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "屏東天氣" in event.message.text:
        a = Pingtung_County()
        b ='\n'.join(a)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif event.message.text == "回答我":
        a = "我盡力了"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token,message)
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)


