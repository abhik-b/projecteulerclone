from django.contrib import admin
from .models import Question
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qshort', 'difficulty_level', 'id')


admin.site.register(Question, QuestionAdmin)
