from django.shortcuts import render

def login(request):
    context = {
        'title': 'Econo - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Econo - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Econo - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...


