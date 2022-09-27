from django.contrib import admin
from django.urls import path
from disciplina import views as view_disciplinas
from question import views as view_question
from answer import views as view_answer
from prova import views as view_prova

urlpatterns = [
    path('admin/', admin.site.urls),

    path('prova/new/', view_prova.create, name='prova'),
    path('prova/new/<str:id>/', view_prova.prova, name='prova'),
    path('prova/list/', view_prova.list_provas, name='prova'),

    path('disciplina/new/', view_disciplinas.create, name='disciplinas'),
    path('disciplina/list/', view_disciplinas.list_disciplinas, name='disciplinas'),

    path('question/new/', view_question.create, name='question'),
    path('question/list/', view_question.list_questions, name='question'),

    path('answer/new/', view_answer.create, name='answer'),
    path('answer/list/', view_answer.list_answers, name='answer'),
]
