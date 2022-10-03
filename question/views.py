from django.shortcuts import render, redirect
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
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save()
        return redirect(f'/prova/new/{question.prova.id}')
    return render(request, 'create_question.html', {'form': form})

