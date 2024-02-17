from django.urls import path,include
from user_app import views
from django.contrib.auth import views as auth_views
from.views import custom_login
from.views import custom_logout


urlpatterns = [
path('register', views.register, name='register'),
path('login/',custom_login, name='login'),
path('logout/',custom_logout,name='logout')
]