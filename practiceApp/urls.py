from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('yoga1',views.yoga1, name='yoga1'),
    path('yoga2',views.yoga2, name='yoga2'),
    path('yoga3',views.yoga3, name='yoga3')
]