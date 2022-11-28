from django.urls import path
from disciplina.views import *

app_name = 'disciplina_urls'
urlpatterns = [
    path('new/', create, name='disciplinas_create'),
    path('delete/<uuid:id>', delete, name='disciplinas_delete'),
]
