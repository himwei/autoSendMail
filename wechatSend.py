import json
import requests
import os


appID = os.environ["AppID"]
appSecret = os.environ["AppSecret"]
openId1 = os.environ["OpenId1"]
openId2 = os.environ["OpenId2"]
templateId = os.environ["TemplateId"]

def get_access_token():
    # 获取access token的url
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}' \
        .format(appID.strip(), appSecret.strip())
    response = requests.get(url).json()
    # print(response)
    access_token = response.get('access_token')
    return access_token

def send_weather(access_token):
    # touser 就是 openID
    # template_id 就是模板ID
    # url 就是点击模板跳转的url
    # data就按这种格式写，time和text就是之前{{time.DATA}}中的那个time，value就是你要替换DATA的值

    body1 = {
        "touser": openId1.strip(),
        "template_id": templateId.strip(),
        "url": "https://weixin.qq.com",
        "data": {
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print(requests.post(url, json.dumps(body1)).text)


    body2 = {
        "touser": openId2.strip(),
        "template_id": templateId.strip(),
        "url": "https://weixin.qq.com",
        "data": {
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
    print(requests.post(url, json.dumps(body2)).text)

if __name__ == "__main__":
    send_weather(get_access_token())