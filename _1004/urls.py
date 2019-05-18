from django.contrib import admin
from django.urls import path
from _1004 import views
app_name = "_1004"


urlpatterns = [
    path('', views.index, name="index"),
]