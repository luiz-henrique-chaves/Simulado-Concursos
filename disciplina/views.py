from django.shortcuts import render, redirect, get_object_or_404
from .models import DisciplinaModel
from .forms import DisciplinaForm

def create(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_urls:materias_master_user')
    return render(request, 'create_disciplina.html', {'form': form})


def delete (request, id):
    context = {}

    obj = get_object_or_404(DisciplinaModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect("core_urls:materias_master_user")
    
    return render(request, 'delete_view.html', context)



