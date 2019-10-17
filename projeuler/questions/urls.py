from django.urls import path
from .views import checkAnswer, questionDetailView, questionListView
app_name = 'questions'
urlpatterns = [
    # path('', QuestionList.as_view(), name='question_list'),
    path('', questionListView, name='question-list'),
    # path('<pk>', QuestionDetail.as_view(), name='question_detail'),
    path('<int:id>/', questionDetailView, name='question-detail'),
    path('checkanswer/<int:id>/', checkAnswer, name='checkanswer'),
]
