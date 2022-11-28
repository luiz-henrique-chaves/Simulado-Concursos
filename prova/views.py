from django.shortcuts import render, redirect, get_object_or_404
from .models import ProvaModel
from .forms import ProvaForm
from question.models import QuestionModel
from answer.models import AnswerModel
from disciplina.models import DisciplinaModel
from django.db import transaction

def prova(request, id):
    dataset = get_object_or_404(ProvaModel, pk=id)
    return render(request, 'prova.html', {'dataset': dataset})

@transaction.atomic
def provaContinue(request):
    if request.method == 'POST':
        data = request.POST
        prova = get_object_or_404(ProvaModel, id=data['id_prova'])
        
        try:
            with transaction.atomic():
                question = QuestionModel.objects.create(
                    issue = data['issue'],
                    prova = prova,
                )
                
                as_respostas = AnswerModel.objects.create(
                    a = data['a'],
                    b = data['b'],
                    c = data['c'],
                    d = data['d'],
                    alternative_correct = data['alternative_correct'],
                    question  = question,
                )
        except Exception as e:
            print(e)

        return redirect("prova_urls:list_answers_por_materias", request.POST['id_prova'])

def list_provas(request):
    form = ProvaForm(request.POST or None)
    return render(
        request,
        'list_provas.html',
        {
            'dataset': ProvaModel.objects.all(),
            'form': form,
            'materias' : DisciplinaModel.objects.all(),
        }
    )

def todas_as_provas_por_materias(request, id):
    return render(
        request,
        'masteruser/todas_as_provas_por_materia.html',
        {'provas': ProvaModel.objects.all().filter(disciplina=id)}
    )

def create(request):
    form = ProvaForm(request.POST or None)
    if form.is_valid():
        prova = form.save()
        return redirect(f'/prova/{prova.id}')
    return render(request, 'create_prova.html', {'form': form})


def delete (request, id):
    context = {}

    obj = get_object_or_404(ProvaModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect("prova_urls:prova_list")
    
    return render(request, 'delete_view.html', context)

