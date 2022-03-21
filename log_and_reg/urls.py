from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('log_in/', views.display_login, name= 'log_in'),
    path('register_new/', views.display_registration),
    path('register', views.create_user),
    path('login', views.login),
    # path('welcome', views.welcome),
    path('log_out', views.log_out),
]


