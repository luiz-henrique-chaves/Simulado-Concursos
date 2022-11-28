from django.urls import path
from question.views import *

app_name = 'question_urls'
urlpatterns = [
    path('new/', create, name='question_create'),
    path('list/', list_questions, name='question_list'),
    path('delete/<uuid:id>', delete, name='question_delete'),
]
