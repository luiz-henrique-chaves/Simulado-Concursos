from django.shortcuts import render
from .models import DisciplinaModel
from .forms import DisciplinaForm

def list_disciplinas(request):
    return render(
        request,
        'list_disciplinas.html',
        {'dataset': DisciplinaModel.objects.all()}
    )

def create(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create_disciplina.html', {'form': form})

