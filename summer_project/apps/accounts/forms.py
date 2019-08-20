from django import forms
from django .forms import widgets
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password as auth_check_password
from .models import User

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="密码2",widget=widgets.PasswordInput(attrs={"placeholder":"确认密码"}))
    mobile_captcha = forms.CharField(label="验证码",widget=widgets.TextInput(
        attrs={"style":"width:160px;padding:10px","placeholder":"验证码","error_messages":{"invalid":"验证码错误"}}))

    class Meta:
        model = User
        fields = ['username','mobile','password']
        widgets = {
            'username': widgets.TextInput(attrs={"placeholder":"用户名"}),
            'mobile': widgets.TextInput(attrs={"placeholder":"手机号码"}),
            'password': widgets.PasswordInput(attrs={"placeholder":"密码"})
        }

    # username是否重复django会自动检查，因为它是unique的
    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if data.isdigit():
            raise ValidationError("密码不能全是数字")
        elif len(data) < 8:
            raise ValidationError("密码长度不能小于8")
        else:
            return self.cleaned_data.get("password")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码输入不一致")


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length="24",
                               widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}))
    captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={"style": "width: 160px;padding: 10px", "placeholder": "验证码", "onblur": "check_captcha()",
               "error_messages": {"invalid": "验证码错误"}}))
    password = forms.CharField(label="密 码",
                               widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}))

    def check_password(self):
        print('check password')
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            return user, auth_check_password(password, user.password)
        except:
            return None, False

    def clean_username(self):
        print(self.cleaned_data.get("username"))
        ret = User.objects.filter(username=self.cleaned_data.get("username"))
        if ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名或密码不正确")