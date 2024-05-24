from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# Create your views here.

def index (request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publica=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})
def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
def buscar(request):
    form = Fotografia.objects.filter("data_fotografia").filter(publicada=True)
    if form.is_valid :
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = form.filter(nome__icontains=nome_a_buscar)

        return render('templates/galeria/index.html', {{'form':form,'produto':produto}})
