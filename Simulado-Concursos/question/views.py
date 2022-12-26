from answer.models import AnswerModel
from answer.forms import AnswerForm
from answer.views import create_answer
from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionModel
from .forms import QuestionForm
from disciplina.models import DisciplinaModel
from prova.objectExpose import ExposeObject

def list_questions(request):
    return render(
        request,
        'list_questions.html',
        {
            'dataset': QuestionModel.objects.all(),
            'materias': DisciplinaModel.objects.all(),
        }
    )


def create_question(request, prova):
    """Cria uma questão com base nos dados da solicitação HTTP POST e vincula a prova especificada à questão."""
    question, created = QuestionModel.objects.get_or_create(
        issue=request.POST['issue'],
        prova=prova
    )
    return ExposeObject({'created':created, 'object':question})
        

def delete (request, id):
    context = {}

    obj = get_object_or_404(QuestionModel, id=id)
    copy = obj

    if request.method == 'POST':
        obj.delete()
        return redirect("prova_urls:list_answers_por_materias", copy.prova.id)

def question_answer_update(request, id):
    context = {}
    question = get_object_or_404(QuestionModel, id=id)
    answer = get_object_or_404(AnswerModel, question = question.id)

    form_question = QuestionForm(request.POST or None, instance=question)
    form_answer = AnswerForm(request.POST or None, instance=answer)
    id_prova = question.prova.id  

    if request.method == 'POST':
        if form_question.is_valid() and form_answer.is_valid():
            form_question.save()
            form_answer.save()
            return redirect("prova_urls:list_answers_por_materias", id_prova)
 
    context['form_question'] = form_question
    context['form_answer'] = form_answer

    return render(request, 'update_question_answer.html', context)



