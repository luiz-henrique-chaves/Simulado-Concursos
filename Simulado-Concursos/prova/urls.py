from django.urls import path
from prova.views import *
from answer.views import list_answers_por_materias

app_name = 'prova_urls'
urlpatterns = [
    path('redirect/', continue_prova, name='prova_new_redirect'),
    path('new/', create, name='prova_create'),
    path('delete/<uuid:id>', delete, name='prova_delete'),
    path('new/<uuid:id>/', display_prova, name='prova_new_id'),     
    path('list/', display_prova_list, name='prova_list'),
    path('<uuid:id>/', list_answers_por_materias, name='list_answers_por_materias'),
]