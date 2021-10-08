from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('saveform', views.saveform, name='saveform'),
    path('sedit', views.sedit, name='sedit'),
    path('seditform',views.seditform,name='seditform'),
    path('delete', views.delete, name='delete'),
]