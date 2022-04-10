from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def index(request):
    return render(request, 'index/index.html')

def charts(request):
    return render(request, 'index/charts.html')

def register(request):
    if request.POST:
        # username = '_'.join([request.POST.get('first_name'), request.POST.get('last_name')])
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat = request.POST.get('repeat')
        email = request.POST.get('email')
        # print(username, password, repeat, email)
        if password != repeat:
            return render(request, 'index/register.html', {'message': 'passwords do not match!'})
        if password is None:
            return render(request, 'index/register.html', {'message': 'password cat not be empty!'})
        try:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return redirect('/')
        except IntegrityError:
            return render(request, 'index/register.html', {'message': 'user is taken'})
    return render(request, 'index/register.html')

def logout_cust(request):
    logout(request)
    return redirect('login')


def login_cust(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'index/login.html', {'message': 'user is not exist'})
    return render(request, 'index/login.html')

def diagram_update(request):
    result = {
        'data': [100, 320, 453, 234, 553, 665, 345, 123, 432, 545, 654, 345, 332, 456, 234],
        'labels': ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2323"],}
    return JsonResponse(result, status=200)


# 'login': ['dimon@gmail.com'], 'password': ['123456']}>