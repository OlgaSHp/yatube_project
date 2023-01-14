from django.urls import path

from . import views

urlpatterns = [
    #главная страницв
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),

]