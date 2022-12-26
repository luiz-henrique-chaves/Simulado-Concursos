from turtle import title
from django.db import models
import uuid

class DisciplinaModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=70)
    
    def __str__(self) -> str:
        return self.title