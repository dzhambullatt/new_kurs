from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'women/index.html', {'title': 'Home Page'})


def about(request):
    return render(request, 'women/about.html', {'title': 'About Page'})


#def categories(request, catid):
#    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")