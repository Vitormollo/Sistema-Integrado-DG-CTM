from django.urls import path
from . import views

app_name = 'assistido'

urlpatterns = [
    path('', views.assistido_view, name='assistidos'),
    path('assistido/', views.assistido_view, name='assistido'),
]
