from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from app01.myforms.register_forms import RegForm
from app01 import models
from django.http import JsonResponse


class Register(View):

    def get(self, request):
        register_forms_obj = RegForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        print(request.POST)
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
        else:
            back_dic['code'] = 10001
            back_dic['msg'] = user_obj.errors
        return JsonResponse(back_dic, safe=False)
