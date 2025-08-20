from django.shortcuts import get_object_or_404, redirect

def editar_assistido(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    if request.method == 'POST':
        assistido.nmcompleto_assist = request.POST.get('nmcompleto_assist', assistido.nmcompleto_assist)
        assistido.numero_assist = request.POST.get('numero_assist', assistido.numero_assist)
        assistido.dn_assist = request.POST.get('dn_assist', assistido.dn_assist)
        assistido.rua_assist = request.POST.get('rua_assist', assistido.rua_assist)
        assistido.numerocasa_assist = request.POST.get('numerocasa_assist', assistido.numerocasa_assist)
        assistido.bairro_assist = request.POST.get('bairro_assist', assistido.bairro_assist)
        assistido.cidade_assist = request.POST.get('cidade_assist', assistido.cidade_assist)
        assistido.nmresponsavel_assist = request.POST.get('nmresponsavel_assist', assistido.nmresponsavel_assist)
        assistido.outro_responsavel = request.POST.get('outro_responsavel', assistido.outro_responsavel)
        assistido.nmgenitor_assist = request.POST.get('nmgenitor_assist', assistido.nmgenitor_assist)
        assistido.nmgenitora_assist = request.POST.get('nmgenitora_assist', assistido.nmgenitora_assist)
        assistido.escola_assist = request.POST.get('escola_assist', assistido.escola_assist)
        assistido.gestante_assist = request.POST.get('gestante_assist', 'False') == 'True'
        assistido.save()
        return redirect('assistido:assistidos')
    return redirect('assistido:assistidos')
from django.shortcuts import render
from assistido.models import Assistido

def assistido_view(request):
    q = request.GET.get('q', '').strip()
    if q:
        assistidos = Assistido.objects.filter(nmcompleto_assist__icontains=q)
    else:
        assistidos = Assistido.objects.all()
    return render(request, 'assistido/assistidos.html', {
        'pagina_atual': 'assistidos',
        'page_title': 'Assistidos',
        'assistidos': assistidos,
        'request': request
    })


