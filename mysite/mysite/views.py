from django.http import HttpResponse
from django.shortcuts import render

def here(request):
    return HttpResponse('媽，我在這!')

def add(request, a, b): # <- 加入這個函式
    s = int(a) + int(b)
    return HttpResponse(s)

def math(request, a, b): # 加入
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render(request,'math.html', locals())

def menu(request):
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foods = [food1, food2]
    return render(request,'menu.html', locals())