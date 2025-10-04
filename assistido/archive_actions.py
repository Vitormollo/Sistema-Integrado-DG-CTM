from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from assistido.models import Assistido
from django.utils import timezone

@require_POST
def arquivar_morto_assistido(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    assistido.arquivomorto_assist = True
    assistido.dtarquivomorto_assist = timezone.now().date()
    assistido.save()
    return redirect('assistido:assistidos')

@require_POST
def desarquivar_morto_assistido(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    assistido.arquivomorto_assist = False
    assistido.dtarquivomorto_assist = None
    assistido.save()
    return redirect('assistido:assistidos')
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from assistido.models import Assistido

@require_POST
def arquivar_assistido(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    assistido.arquivado_assist = True
    assistido.id_conselheira = None
    assistido.save()
    return redirect('assistido:assistidos')

@require_POST
def desarquivar_assistido(request, id_assist):
    assistido = get_object_or_404(Assistido, id_assist=id_assist)
    assistido.arquivado_assist = False
    assistido.save()
    return redirect('assistido:assistidos')
