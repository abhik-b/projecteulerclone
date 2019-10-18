from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text',
                  'answer_text',
                  'difficulty_level', ]
