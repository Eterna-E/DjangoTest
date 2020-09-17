from django.shortcuts import render

# Create your views here.
def menu(request):
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foody = food1.items()
    foods = [food1, food2]
    return render(request,'menu.html', locals())