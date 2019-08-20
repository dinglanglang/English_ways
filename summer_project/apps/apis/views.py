# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse,HttpResponse
from django.core.cache import cache
from libs import sms
from io import BytesIO
from libs import patcha
import base64
from django.shortcuts import render
import random,logging

logger = logging.getLogger("apis")


def get_mobile_captcha(request):
    ret = {"code":200,"msg":"验证码发送成功！"}
    try:
        #获取ajax-用户提交的数据
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        #生产随机验证码
        mobile_captcha = "".join(random.choices('0123456789',k=6))
        #将短信验证码写入redis,300s过期
        cache.set(mobile,mobile_captcha,300)
        #发送短信
        logger.info("验证码是{}".format(mobile_captcha))
        if not sms.send_sms(mobile,mobile_captcha):
            raise ValueError("发送短信失败")
    except Exception as ex:
        logger.error(ex)
        ret = {"code":400, "msg":"验证码发送失败！"}
    return JsonResponse(ret)

def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type+base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)

def check_captcha(request):
    ret = {"code":400, "msg":"验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code',"")
    session_captcha_code = request.session.get['captcha_code',""]
    print(post_captcha_code, session_captcha_code)
    if post_captcha_code and post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)

import os,time,datetime,base64
from summer_project.settings import MEDIA_ROOT,MEDIA_URL
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class ChangeAvator(LoginRequiredMixin, View):
    def post(self, request):
        today = datetime.date.today().strftime("%Y%m%d")
        # 图片的data-img格式=>data:image/jpg;base64,xxxx
        img_src_str = request.POST.get("image")
        img_str = img_src_str.split(',')[1]
        # 取出格式:jpg/png...
        img_type = img_src_str.split(';')[0].split('/')[1]
        # 取出数据:转化为bytes格式
        img_data = base64.b64decode(img_str)
        # 相对上传路径: 头像上传的相对路径
        avator_path = os.path.join("avator",today)
        # 绝对上传路径：头像上传的绝对路径
        avator_path_full = os.path.join(MEDIA_ROOT, avator_path)
        if not os.path.exists(avator_path_full):
            os.mkdir(avator_path_full)
        filename = str(time.time())+"."+img_type
        # 绝对文件路径，用于保存图片
        filename_full = os.path.join(avator_path_full, filename)
        # 相对MEDIA_URL路径，用于展示数据
        img_url = "{}{}/{}".format(MEDIA_URL,avator_path,filename)
        try:
            with open(filename_full, 'wb') as fp:
                fp.write(img_data)
            ret = {
                "result": "ok",
                "file": img_url
            }
        except Exception as ex:
            ret = {
                "result": "error",
                "file": "upload fail"
            }
        request.user.avator_sor = os.path.join(avator_path,filename)
        request.user.save()
        return JsonResponse(ret)