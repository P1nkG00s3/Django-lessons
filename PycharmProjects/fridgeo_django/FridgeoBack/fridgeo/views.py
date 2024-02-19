from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [
    {'title': "Информация", 'url_name': 'information'},
    {'title': "Регистрация/Вход", 'url_name': 'login'},
    {'title': "Аккаунт", 'url_name': 'account'},
]

data_dp = [
    {'id': 1, 'title': 'Хумус', 'content': 'Это рецепт хумуса', 'is_published': True},
    {'id': 2, 'title': 'Рис', 'content': 'Это рецепт риса', 'is_published': True},
    {'id': 3, 'title': 'Пюре', 'content': 'Это рецепт пюре', 'is_published': True}
]


def index(request):
    data = {
        'menu': menu,
        'receipt': data_dp
    }
    return render(request, 'fridgeo/index.html', context=data)



def HelloThere(request):
    return HttpResponse(
        "<div class=\"wrapper\"> <div class=\"name\">CALCULATOR</div><section class=\"screen\">  0 </section>")


def show_post(request, post_id):
    return HttpResponse(f'<p>Статья с номером {post_id}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def information(request):
    return render(request, 'fridgeo/information.html')


def login(request):
    return HttpResponse('<h1>Это регистрация/вход</h1>')


def account(request):
    return HttpResponse('<h1>Это ваш аккаунт</h1>')
