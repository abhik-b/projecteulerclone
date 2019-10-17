from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.CharField(max_length=500)
    difficulty_level = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def qshort(self):
        return self.question_text[0:30]+'....'
