from django.shortcuts import render, HttpResponse, redirect,reverse
from app01 import models


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.Userinfo.objects.filter(username=username, password=password).first()
        if user_obj.password == password and user_obj.username == username:
            return HttpResponse('登陆成功')
        return HttpResponse('用户名或密码错误')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.Userinfo.objects.filter(username=username, password=password).first()
        if user_obj:
            return HttpResponse('用户名已注册')
        models.Userinfo.objects.create(username=username, password=password)
        return redirect('/login/')
    return render(request, 'register.html')


def user_all(request):
    user_obj_all = models.Userinfo.objects.all()
    # print(user_obj_all)
    return render(request, 'user_all.html', locals())


def edit(request):
    user_id = request.GET.get('user_id')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.Userinfo.objects.filter(id=user_id).update(username=username,password=password)
        return redirect(reverse('user_all'),)
    user_obj = models.Userinfo.objects.filter(id=user_id).first()
    return render(request, 'edit.html', locals())



