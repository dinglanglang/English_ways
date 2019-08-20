import urllib.request
import urllib
import json
import logging

logger = logging.getLogger('apis')

def send_sms(mobile,captcha):
    flag = True
    url = "https://open.ucpaas.com/ol/sms/sendsms"
    headers = {
        "Content-Type":"application/json;charset=utf-8"
    }
    values = {
        "sid":"6c32b1ab0df397d14b18b4f599671730",
        "token":"245679ca256fd3af201df51c3eed8d7c",
        "appid":"473e1cb2d207447b802ac5345a4c5a7d",
        "templateid":"489851",
        "param":"{},300".format(str(captcha)),
        "mobile":mobile,
    }

    try:
        data = json.dumps(values).encode('utf-8')
        logger.info("即将发送短信：{}".format(data))
        #创建一个request，放入我们的地址，数据，头部信息
        request = urllib.request.Request(url,data,headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        code = json.loads(html)["code"]
        if code == "000000":
            logger.info("短信发送成功：{}".format(html))
            flag = True
        else:
            logger.info("短信发送失败：{}".format(html))
            flag = False
    except Exception as ex:
        logger.info("出错了，错误原因：{}".format(ex))
        flag = False
    return flag


# if __name__ == "__main__":
#     send_sms("15570871629","123456")
