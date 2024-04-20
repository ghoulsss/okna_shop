from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'ECONO - Главная',
        'content': 'Магазин окон ECONO'

    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'ECONO - О нас',
        'content': 'О нас',
        'text_on_page': 'Ваше счастье и красивый вид -- наше работа'

    }
    return render(request, 'main/about.html', context=context)