from django.db import models
from disciplina.models import DisciplinaModel
from prova.models import ProvaModel
import uuid

class QuestionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.TextField()
    prova = models.ForeignKey(ProvaModel, on_delete=models.CASCADE)
    

    def __str__ (self):
        return self.issue
    
