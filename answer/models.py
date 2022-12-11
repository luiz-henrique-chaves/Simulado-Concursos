from django.db import models
from question.models import QuestionModel
import uuid

class AnswerModel(models.Model):
    ALTERNATIVES_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    a = models.TextField(max_length=200)
    b = models.TextField(max_length=200)
    c = models.TextField(max_length=200)
    d = models.TextField(max_length=200)
    alternative_correct = models.CharField(max_length=1, choices=ALTERNATIVES_CHOICES, blank=False, null=False)
    explanation = models.TextField(max_length=1650)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

