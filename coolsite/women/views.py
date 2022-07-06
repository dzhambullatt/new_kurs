from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница Приложения Women")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")