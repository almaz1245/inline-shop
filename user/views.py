from django.shortcuts import render
from .models import User
from .forms import LoginForm, RegistrationForm, UserPortfileForm
from django.http import HttpResponseRedirect
from django.contrib import auth,messages
# Create your views here.


def  authen(req):
    if req.method == 'POST':
        form = RegistrationForm(data = req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(req, 'auth.html', context)


def sign_up(req):
    if req.method == 'POST':
        form = LoginForm(data=req.POST)
        if form.is_valid():
            username = req.POST['username']
            password = req.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(req, user)
                messages.success(req,f'{username} вы успешно прошли авторизатцию')
                return HttpResponseRedirect('/')
    else: 
        print('else')
        form = LoginForm()
    context = {'form':form}
    return render(req,'sign_up.html',context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')