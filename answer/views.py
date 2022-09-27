from django.shortcuts import render
from .forms import AnswerForm
from .models import AnswerModel

def list_answers(request):
    return render(
        request,
        'list_answers.html',
        {'dataset': AnswerModel.objects.all()}
    )

def create(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create.html', {'form': form})


