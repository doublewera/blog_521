from django.urls import path
from . import views

urlpatterns = [
    path('<int:uid>/', views.posts, name='blogpost'),
]