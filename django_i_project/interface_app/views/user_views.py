import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from interface_app.forms.user_form import UserForm

from interface_app.libs.response import response_success, response_failed, ErrorCode


@require_http_methods(['POST'])
def user_login(request, *args, **kwargs):
    """ 登录 """
    body = request.body
    print('body---------------->', body)
    data = json.loads(body, encoding='utf-8')
    print('data--------------->', data)

    form = UserForm(data)
    if not form.is_valid():
        return response_failed()

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    print('等待user验证......................')
    user = authenticate(username=username, password=password)
    print('user-------------->', user)
    if not user:
        print('没有进到user')
        return response_failed(code=ErrorCode.auth, message='登录失败')
    else:
        login(request, user)
        print('进入到user，并且登录成功')
        return response_success()



@require_http_methods(['POST'])
def user_register(request, *args, **kwargs):
    """ 注册 """
    body = request.body
    data = json.loads(body, encoding='utf-8')

    form = UserForm(data)
    if not form.is_valid():
        return response_failed()

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    if User.objects.filter(username=username).exists():
        return response_failed(code=ErrorCode.auth, message='用户名已存在')

    user = User.objects.create_user(username=username, password=password)
    if user:
        login(request, user)
        return response_success()
    else:
        return response_failed(code=ErrorCode.auth, message='登录失败')

@require_http_methods(['DELETE'])
def user_logout(request, *args, **kwargs):
    """ 退出 """
    logout(request)
    return response_success()

@require_http_methods(['GET'])
def get_user_info(request, *args, **kwargs):
    user = request.user
    if not user:
        return response_failed(code=ErrorCode.auth, message='用户未登录')
    if user.is_authenticated:
        return response_success(data={
            'id':user.id,
            'name':user.username
        })
    else:
        return response_failed(code=ErrorCode.auth, message='用户未登录')