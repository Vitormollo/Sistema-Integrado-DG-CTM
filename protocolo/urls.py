from django.urls import path
from . import views

app_name = 'protocolo'

urlpatterns = [
    path('', views.protocolos, name='protocolos'),
]
