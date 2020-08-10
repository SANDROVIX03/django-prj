from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import *


def listar_obra(request, template_name="obra_list.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get("ordenar", '')
    if query:
        obra = OBRA.objects.filter(NOM_OBRA__icontains=query)
    else:
        try:
            if ordenar:
                obra = OBRA.objects.all().order_by(ordenar)
            else:
                obra = OBRA.objects.all()
            obra = Paginator(obra, 2)
            obra = obra.page(page)
        except PageNotAnInteger:
            obra = obra.page(1)
        except EmptyPage:
            obra = paginator.page(paginator.num_pages)
    obras = {'lista': obra}
    return render(request, template_name, obras)

def perfil_obra(request, pk, template_name="perfil_obra.html"):
    obra = get_object_or_404(OBRA, pk=pk)
    return render(request, template_name, {'obra': obra})