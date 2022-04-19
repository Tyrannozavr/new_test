from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from diagrams.models import *
from .forms import Current_value
from time import time


def index(request):
    now = time()
    return render(request, 'index/index.html', {'now': now})

def charts(request):
    form = Current_value()
    if request.user.username == 'user_one':
         model = Ai_one
    elif request.user.username == 'user_two':
        model = Ai_two
    else:
        return redirect('/')
    if request.POST:
        if request.POST.get('update'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.sts = 2
            obj.save()
        elif request.POST.get('create'):
            current = request.POST.get('current', 0)
            sts = request.POST.get('sts', 0)
            model.objects.create(current=current, sts=sts)
        elif request.POST.get('delete'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.delete()
    a = model.objects.all().order_by('id')
    data = a
    categories = [f"{i.id}" for i in a]
    values = [float(i.current) for i in a]
    return render(request, 'index/charts.html', {'form':form, 'data':data, 'categories':categories, 'values':values})


def diagram_json(request):
    if request.user.username == 'user_one':
         model = Ai_one
    elif request.user.username == 'user_two':
        model = Ai_two
    else:
        return redirect('/')
    a = model.objects.all().order_by('id')
    labels = [f"{i.id}" for i in a]
    values = [float(i.current) for i in a]
    # labels = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2323"]
    # values = [100, 320, 453, 234, 553, 665, 345, 123, 432, 545, 654, 345, 332, 456, 234]
    result = {
        'values': values,
        'labels': labels,}

    return JsonResponse(result, status=200)


def register(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat = request.POST.get('repeat')
        email = request.POST.get('email')

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

def diagrams(request):
    if request.user.username == 'user_one':
         model = Ai_one
    elif request.user.username == 'user_two':
        model = Ai_two
    else:
        return redirect('/')
    if request.POST:
        if request.POST.get('update'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.sts = 2
            obj.save()
        elif request.POST.get('create'):
            current = request.POST.get('current', 0)
            sts = request.POST.get('sts', 0)
            model.objects.create(current=current, sts=sts)
        elif request.POST.get('delete'):
            id = int(request.POST.get('id'))
            obj = model.objects.get(id=id)
            obj.delete()
    a = model.objects.all()
    data = a
    categories = [f"{i.id}" for i in a]
    values = [float(i.current) for i in a]
    form = Current_value()
    return render(request, 'diagrams/diagrams.html', {'categories': categories, 'values': values, 'data': data, 'form':form})