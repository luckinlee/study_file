from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from app01.myforms.register_forms import RegForm
from app01 import models
from django.http import JsonResponse
from app01.common.code import ret_code_img
from django.contrib import auth


class Register(View):

    def get(self, request):
        register_forms_obj = RegForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        user_obj = RegForm(request.POST)
        back_dic = {'code': 200, 'msg': '成功', 'url': '/login/'}
        if user_obj.is_valid():
            print(user_obj.cleaned_data)
            clean_data = user_obj.cleaned_data
            clean_data.pop('re_password')
            file_obj = request.FILES.get('avatar')
            if file_obj:
                clean_data['avatar'] = file_obj
            models.UserInfo.objects.create_user(**clean_data)
            back_dic['url'] = '/login/'
        else:
            back_dic['code'] = 10001
            back_dic['msg'] = user_obj.errors
        return JsonResponse(back_dic, safe=False)


class Login(View):

    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        back_dict = {}
        if request.session.get('code').lower() == code.lower():
            user_obj = auth.authenticate(request, username=username, password=password)
            if user_obj:
                auth.login(request, user_obj)
                back_dict['url'] = '/home/',
            else:
                back_dict['error_code'] = 10001
                back_dict['msg'] = '用户名或密码不正确'
        else:
            back_dict['error_code'] = 10002
            back_dict['msg'] = '验证码不正确'
        return JsonResponse(back_dict, safe=False)


# 验证码
def get_code(request):
    code, img = ret_code_img()
    ret = HttpResponse(img)
    request.session['code'] = code
    return ret


def set_password(request):
    back_dic = {}
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        is_correct = request.user.check_password(old_password)
        if is_correct:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                back_dic['msg'] = '修改成功'
            else:
                back_dic['code'] = 1001
                back_dic['error_msg'] = '两次密码不一致'
        else:
            back_dic['code'] = 1002
            back_dic['error_msg'] = '原密码输入有误'
        return JsonResponse(back_dic)


class home(View):

    def get(self, request):
        return render(request, 'home.html', locals())
