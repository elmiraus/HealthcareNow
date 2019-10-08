from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('chooseplan',views.chooseplan, name='chooseplan'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
]
