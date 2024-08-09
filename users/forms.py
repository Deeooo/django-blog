from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# 用户注册表单
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # model属性表示这个表单类与User模型关联
        # fields属性是一个列表，包含了表单类中需要显示的字段
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# 用户更新表单(用户名、邮箱)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # model属性表示这个表单类与User模型关联
        # fields属性是一个列表，包含了表单类中需要显示的字段
        model = User
        fields = ['username', 'email']


# 用户更新表单(图片)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
