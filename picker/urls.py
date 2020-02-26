from . import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path('', views.mainpage, name="mainPage"),
    path('inputPage/', views.inputPage, name="inputPage"),
    path('result/', views.resultPage, name="resultPage"),
    path('credit/', views.creditPage, name="creditPage"),
    path('predict/sample1/', views.sample1predict, name="sample1"),
    path('predict/sample2/', views.sample2predict, name="sample2"),
    path('tftest', views.tftest),
    path('errorPage', views.errorPage, name="errorPage"),
]

