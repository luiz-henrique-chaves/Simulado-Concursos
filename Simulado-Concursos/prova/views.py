from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ProvaModel
from .forms import ProvaForm
from question.views import create_question
from answer.views import create_answer
from disciplina.models import DisciplinaModel
from django.contrib import messages

def display_prova(request, id):
    """Renderiza o template da prova e passa os dados da prova como contexto."""
    try:
        dataset = ProvaModel.objects.get(pk=id)
    except ProvaModel.DoesNotExist:
        raise Http404
    return render(request, 'prova.html', {'dataset': dataset})



def continue_prova(request):
    """
    Recupera a prova com base no ID fornecido na solicitação HTTP POST 
    e cria uma questão com base nos dados da solicitação HTTP POST.

    Esta etapa é fundamental para não criar questões com ID's não existentes.
    """
    prova = get_object_or_404(ProvaModel, pk=request.POST['id_prova'])
    question = create_question(request, prova)
    answer = create_answer(request, question.object)
    
    if (question.created and answer.created):
        messages.success(request, 'A questão foi salva com sucesso!')
        return redirect('prova_urls:list_answers_por_materias', request.POST['id_prova'])
    else:
        messages.success(request, 'Houve um problema ao salvar a questão, contate o desenvolvedor para resolver este bug.')
        return redirect('prova_urls:list_answers_por_materias', request.POST['id_prova'])
    



def display_prova_list(request):
    """Renderiza o template da lista de provas e passa a lista de provas e o formulário de prova como contexto."""
    form = ProvaForm(request.POST or None)
    return render(request, 'list_provas.html', {
        'dataset': ProvaModel.objects.all(),
        'form': form,
        'materias': DisciplinaModel.objects.all()
    })



def display_all_provas_by_subject(request, id):
    """Renderiza o template da lista de provas por matéria e passa a lista de provas como contexto."""
    disciplina = get_object_or_404(DisciplinaModel, pk=id)
    return render(request, 'masteruser/todas_as_provas_por_materia.html', {'provas': disciplina.provas.all()})



def create(request):
    form = ProvaForm(request.POST or None)
    if form.is_valid():
        prova = form.save()
        return redirect('/prova/{}'.format(prova.id))
    return redirect("prova_urls:prova_list")



def delete(request, id):
    obj = get_object_or_404(ProvaModel, pk=id)

    if request.method == 'POST':
        obj.delete()
        return redirect("prova_urls:prova_list")

    return render(request, 'delete_view.html')



# Atualiza para a mesma página de origem da requisição:
# redirect(request.META['HTTP_REFERER'])