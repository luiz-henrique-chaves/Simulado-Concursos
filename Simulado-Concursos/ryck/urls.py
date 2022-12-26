from django.contrib import admin
from django.urls import path, include
from disciplina import views as view_disciplinas
from question import views as view_question
from answer import views as view_answer
from core.views import *


urlpatterns = [
    path('master/', admin.site.urls),
    path('', TemplateIndex, name='templateIndex'),
    path('admin/', include('core.urls') ),
    path('prova/', include('prova.urls') ),
    path('question/', include('question.urls') ),
    path('disciplina/', include('disciplina.urls') ),
    path('answer/', include('answer.urls') ),
]
