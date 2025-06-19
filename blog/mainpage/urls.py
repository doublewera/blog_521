from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path(
        'login/',                               # путь в браузере
        auth_views.LoginView.as_view(           # django login
            template_name='user/login.html'),   # шаблон
        name='login'),                          # {% url name %}
    path('logout/',
        auth_views.LogoutView.as_view(
        next_page='/'),
        name='logout'),
    path('register/', views.register, name='register'),
]
