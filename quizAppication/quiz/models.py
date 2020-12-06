from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuizModel(models.Model):
    quiz_name = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)

class Question(models.Model):
    question_string = models.CharField(max_length=100)

class QuizQuestionMap(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ScoreModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)