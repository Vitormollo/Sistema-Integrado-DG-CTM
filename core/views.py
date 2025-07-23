def dashboard_view(request):
    return render(request, 'core/dashboard.html', {
        'page_title': 'Início',
        'pagina_atual': 'dashboard'
    })
from django.shortcuts import render

from django.shortcuts import redirect

def home_view(request):
    return redirect('usuario:login')

def configuracao_view(request):
    return render(request, 'core/configuracao.html', {
        'page_title': 'Configurações',
        'pagina_atual': 'configuracao'
    })
# Create your views here.
