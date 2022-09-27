from django.shortcuts import render, redirect, get_object_or_404
from .models import ProvaModel
from .forms import ProvaForm

def prova(request, id):
    dataset = get_object_or_404(ProvaModel, pk=id)
    return render(request, 'prova.html', {'dataset': dataset})

def list_provas(request):
    return render(
        request,
        'list_provas.html',
        {'dataset': ProvaModel.objects.all()}
    )

def create(request):
    form = ProvaForm(request.POST or None)
    if form.is_valid():
        prova = form.save()
        return redirect(f'/prova/new/{prova.id}', test="hum")
    return render(request, 'create.html', {'form': form})



