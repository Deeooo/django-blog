from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# 从Django框架的auth模块中导入logout函数。这个函数主要用于在Web应用程序中处理用户注销操作
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required 是Django框架中的一个装饰器，用于限制未登录用户访问特定视图函数。
# 当用户未登录时，该装饰器会将用户重定向到登录页面，
# 登录成功后，用户将被重定向回原始请求的页面。
from django.contrib.auth.decorators import login_required


# 用户注册
def register(request):
    # 用于处理用户注册的视图函数。当请求方法为POST时，它会创建一个UserCreationForm实例并使用提交的数据填充它。
    # 如果表单有效（即数据符合要求），它将从表单中获取用户名，并向用户发送一条成功创建账户的消息，然后重定向到博客主页。
    # 如果请求方法不是POST，它将创建一个空的UserCreationForm实例。
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # 保存数据到数据库
            # form.cleaned_data是一个字典，包含了经过清理和验证的表单数据。
            # 通过调用get()方法并传入字段名作为参数，你可以安全地访问这些数据，而不必担心数据不存在或未经过验证的情况。
            # 如果指定的字段不存在于cleaned_data字典中，get()方法将返回None。
            username = form.cleaned_data.get('username')
            messages.success(request, f'你的账户创建成功！你现在可以登录。')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # render函数的第一个参数是请求对象（request），第二个参数是模板文件的路径，第三个参数是一个字典，用于将上下文变量传递给模板。
    return render(request, 'users/register.html', {'form': form})


# 用户注销
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


# 个人资料
@login_required  # login_required装饰器默认将未登录的用户重定向到LOGIN_URL设置的登录页面，如果没有设置LOGIN_URL，则默认为/accounts/login/
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'你的账户更新成功！')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
