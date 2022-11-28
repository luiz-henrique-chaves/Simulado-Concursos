from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionModel
from .forms import QuestionForm
from disciplina.models import DisciplinaModel

def list_questions(request):
    return render(
        request,
        'list_questions.html',
        {
            'dataset': QuestionModel.objects.all(),
            'materias': DisciplinaModel.objects.all(),
        }
    )


def create(request):
    return render(request, 'create_question.html')

def delete (request, id):
    context = {}

    obj = get_object_or_404(QuestionModel, id=id)
    copy = obj

    if request.method == 'POST':
        obj.delete()
        return redirect("prova_urls:list_answers_por_materias", copy.prova.id)
    
    #return render(request, 'delete_view.html', context)



