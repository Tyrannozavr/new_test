from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse


def index(request):
    return render(request, 'index/index.html')

def charts(request):
    return render(request, 'index/charts.html')

def diagram_update(request):
    result = {
        'data': [100, 320, 453, 234, 553, 665, 345, 123, 432, 545, 654, 345, 332, 456, 234],
        'label': ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
                  "2012", "2013", "2323"],}
    return JsonResponse(result, status=200)


def aaa(request):
    return render(request, 'hello.html')
