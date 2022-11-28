from django.urls import path
from answer.views import *

app_name = 'answer_urls'
urlpatterns = [
    path('new/', create, name='answer_create'),
    path('list/', list_answers, name='answer_list'),
]
