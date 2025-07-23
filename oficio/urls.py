from django.urls import path
from . import views

app_name = 'oficio'

urlpatterns = [
    path('', views.oficios, name='oficios'),
]
