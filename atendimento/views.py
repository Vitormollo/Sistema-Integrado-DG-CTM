from django.shortcuts import render

def atendimento(request):
    return render(request, 'atendimento/atendimento.html', {
        'pagina_atual': 'atendimento',
        'page_title': 'Atendimentos'
    })
