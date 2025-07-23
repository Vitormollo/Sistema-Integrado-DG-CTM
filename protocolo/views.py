from django.shortcuts import render

def protocolos(request):
    return render(request, 'protocolos.html', {
        'pagina_atual': 'protocolo',
        'page_title': 'Protocolo'
    })
