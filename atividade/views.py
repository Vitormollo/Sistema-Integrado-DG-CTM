from django.shortcuts import render

def log(request):
    return render(request, 'atividade/atividade.html', {
        'pagina_atual': 'atividade',
        'page_title': 'Atividade'
    })
