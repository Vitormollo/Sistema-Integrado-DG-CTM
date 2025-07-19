from django.urls import path
from . import views

app_name = 'atendimento'

urlpatterns = [
    path('', views.atendimento, name='atendimento'),
]
