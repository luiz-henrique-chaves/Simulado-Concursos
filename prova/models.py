from django.db import models
from disciplina.models import DisciplinaModel
import uuid

class ProvaModel (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    disciplina = models.ForeignKey(DisciplinaModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title