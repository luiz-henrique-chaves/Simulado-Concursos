from django.shortcuts import render
from .models import QuestionModel
from .forms import QuestionForm

def list_questions(request):
    return render(
        request,
        'list_questions.html',
        {'dataset': QuestionModel.objects.all()}
    )

def create(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create.html', {'form': form})

