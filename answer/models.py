from django.db import models
from question.models import QuestionModel
import uuid

class AnswerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.TextField(max_length=200)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.answer

