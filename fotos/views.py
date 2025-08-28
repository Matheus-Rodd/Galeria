from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Foto

def lista_fotos(request):
    q = request.GET.get('q', '').strip()
    fotos = Foto.objects.all()
    if q:
        fotos = fotos.filter(
            Q(titulo__icontains=q) | Q(descricao__icontains=q) | Q(local__icontains=q)
        )
    contexto = {
        'fotos': fotos,
        'q': q,
    }
    return render(request, 'fotos/lista.html', contexto)

def detalhe_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'fotos/detalhe.html', {'foto': foto})
