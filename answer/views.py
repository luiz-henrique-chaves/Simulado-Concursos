from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnswerForm
from prova.models import ProvaModel
from .models import AnswerModel
from question.models import QuestionModel
from django.http import Http404

def list_answers(request):
    return render(
        request,
        'list_answers.html',
        {'dataset': AnswerModel.objects.all()}
    )

def list_answers_por_materias(request, id, titulo=None):
    q, provaQueryModel = list(), get_object_or_404(ProvaModel, pk=id)

    if titulo is not None:
        titulo_da_prova = provaQueryModel.title.replace(' ', '-')
        if titulo_da_prova == titulo:
            pass
        else:
            raise Http404("Prova não eoncontrada!")

    
    for question in QuestionModel.objects.all().filter(prova=id):
        answer = AnswerModel.objects.all().filter(question = question.id).first()
        q.append({
            'AnswerModel': {
                'question_id': answer.question.id,
                'question': answer.question.issue,
                'a': answer.a,
                'b': answer.b,
                'c': answer.c,
                'd': answer.d,
                'alternative_correct': answer.alternative_correct,
                'disciplina': answer.question.prova.disciplina.title,
            }
        })
    return render(
        request,
        'list_answers_por_prova.html',
        {'context' : q, 'prova_id': id, 'prova_title': provaQueryModel.title}
    )


def create(request):
    return render(request, 'create_answer.html')
