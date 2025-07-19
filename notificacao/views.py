from django.shortcuts import render, redirect


def is_conselheira(user):
    return user.groups.filter(name='Conselheira').exists()


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('usuario:login')


def notificacao(request):
    return render(request, 'notificacao/notificacao.html', {'pagina_atual': 'notificacao'})

def dashboard_view(request):
    return render(request, 'index.html', {'pagina_atual': 'dashboard'})

