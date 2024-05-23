from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category


def index(request):
    categories = Category.objects.all()
    context = {
        "title": "Home - главная страница",
        "content": "Магазин мебели Home",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - о нас",
        "content": "О нас",
        "text_on_page": "Текст, текст",
    }
    return render(request, "main/about.html", context)
