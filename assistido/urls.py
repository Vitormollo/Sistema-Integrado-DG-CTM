from django.urls import path
from . import views

app_name = 'assistido'

urlpatterns = [
    path('', views.assistido_view, name='assistidos'),
    path('assistido/', views.assistido_view, name='assistido'),
    
    path('editar/<int:id_assist>/', views.editar_assistido, name='editar'),
    path('detalhe/<int:id_assist>/', views.detalhe_assistido, name='detalhe'),
    path('add-irmao/<int:id_assist>/', views.add_irmao, name='add_irmao'),
]
