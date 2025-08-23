from assistido.models import Localizador
from django.utils import timezone

# View para adicionar localização
from django.views.decorators.http import require_POST

@require_POST
def add_local(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    from django.utils import timezone
    destino_local = request.POST.get('destino_local')
    if destino_local:
        Localizador.objects.create(
            id_assist=assistido,
            dt_local=timezone.now().date(),
            destino_local=destino_local
        )
    return redirect('assistido:detalhe', id_assist=assistido.id_assist)
def detalhe_assistido(request, id_assist):
    import json
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    form = AddIrmaoForm(id_assist)
    # Serializa os assistidos disponíveis para autocomplete
    assistidos_list = [
        {'id': a.id_assist, 'nome': a.nmcompleto_assist}
        for a in form.fields['irmao'].queryset
    ]
    assistidos_json = json.dumps(assistidos_list)
    # Buscar irmãos em ambos os lados da relação
    from assistido.models import Irmaos
    irmaos_1 = Irmaos.objects.filter(id_assist_1=assistido).values_list('id_assist_2', flat=True)
    irmaos_2 = Irmaos.objects.filter(id_assist_2=assistido).values_list('id_assist_1', flat=True)
    irmaos_ids = set(irmaos_1).union(set(irmaos_2))
    # Remove o próprio assistido se por acaso estiver na lista
    irmaos_ids.discard(assistido.id_assist)
    irmaos = Assistido.objects.filter(id_assist__in=irmaos_ids)
    # Localizadores do assistido
    localizadores = assistido.localizadores.all().order_by('-dt_local')
    return render(request, 'assistido/detalhe.html', {
        'assistido': assistido,
        'form': form,
        'assistidos_json': assistidos_json,
        'irmaos': irmaos,
        'localizadores': localizadores
    })
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

from assistido.models import Irmaos

# View para adicionar irmão
from django import forms


class AddIrmaoForm(forms.Form):
    irmao = forms.ModelChoiceField(
        queryset=Assistido.objects.none(),
        label="Selecione o irmão",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'data-bs-toggle': 'select2',
            'style': 'width: 100%'
        })
    )

    def __init__(self, id_assist, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ja_irmaos = Irmaos.objects.filter(id_assist_1=id_assist).values_list('id_assist_2', flat=True)
        self.fields['irmao'].queryset = Assistido.objects.exclude(id_assist=id_assist).exclude(id_assist__in=ja_irmaos)


def add_irmao(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    if request.method == 'POST':
        form = AddIrmaoForm(id_assist, request.POST)
        if form.is_valid():
            irmao = form.cleaned_data['irmao']
            Irmaos.objects.create(id_assist_1=assistido, id_assist_2=irmao)
            return redirect('assistido:detalhe', id_assist=assistido.id_assist)
    else:
        form = AddIrmaoForm(id_assist)
    return render(request, 'assistido/add_irmao.html', {'form': form, 'assistido': assistido})

def assistido_view(request):
    q = request.GET.get('q', '').strip()
    if q:
        assistidos = Assistido.objects.filter(nmcompleto_assist__icontains=q)
    else:
        assistidos = Assistido.objects.all()
    # telefones já podem ser acessados via a.telefones.all no template
    return render(request, 'assistido/assistidos.html', {
        'pagina_atual': 'assistidos',
        'page_title': 'Assistidos',
        'assistidos': assistidos,
        'request': request
    })


