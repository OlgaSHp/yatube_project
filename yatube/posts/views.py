from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('Приветствуем на сайте для блогеров!')


def group_posts(request, slug):
    return HttpResponse('Здесь пока пусто, но скоро будет много интересного!')

