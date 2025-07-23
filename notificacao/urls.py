from django.urls import path
from . import views

app_name = 'notificacao'

urlpatterns = [
    path('', views.notificacao, name='notificacao'),
]