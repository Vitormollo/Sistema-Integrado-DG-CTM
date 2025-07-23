
from django.urls import path
from . import views

app_name = 'atividade'

urlpatterns = [
    path('', views.log, name='index'),
]
