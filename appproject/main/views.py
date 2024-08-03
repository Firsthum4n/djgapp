from django.shortcuts import render
from .models import *

menu = ['Главная', 'Профиль', 'Войти']


def index_page(request):
    posts = Heroes.objects.all()
    return render(request, 'main/index.html', {'menu': menu, 'title': 'HG', 'posts': posts})
