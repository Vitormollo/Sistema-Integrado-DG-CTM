from django.urls import path
from . import views
from . import archive_actions

app_name = 'assistido'

urlpatterns = [
    path('deletar/<int:id_assist>/', views.deletar_assistido, name='deletar'),
    path('arquivar-morto/<int:id_assist>/', archive_actions.arquivar_morto_assistido, name='arquivar_morto'),
    path('desarquivar-morto/<int:id_assist>/', archive_actions.desarquivar_morto_assistido, name='desarquivar_morto'),
    path('', views.assistido_view, name='assistidos'),
    path('assistido/', views.assistido_view, name='assistido'),
    path('editar/<int:id_assist>/', views.editar_assistido, name='editar'),
    path('detalhe/<int:id_assist>/', views.detalhe_assistido, name='detalhe'),
    path('add-irmao/<int:id_assist>/', views.add_irmao, name='add_irmao'),
    path('remover-irmao/<int:id_assist>/<int:id_irmao>/', views.remover_irmao, name='remover_irmao'),
    path('add-local/<int:id_assist>/', views.add_local, name='add_local'),
    path('cadastrar/', views.cadastrar_assistido, name='cadastrar'),
    path('arquivar/<int:id_assist>/', archive_actions.arquivar_assistido, name='arquivar'),
    path('desarquivar/<int:id_assist>/', archive_actions.desarquivar_assistido, name='desarquivar'),
]
