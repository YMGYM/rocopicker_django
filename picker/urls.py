from . import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path('', views.mainpage, name="mainPage"),
    path('inputPage/', views.inputPage, name="inputPage"),
    path('result/', views.resultPage, name="resultPage"),
    path('credit/', views.creditPage, name="creditPage"),
]

