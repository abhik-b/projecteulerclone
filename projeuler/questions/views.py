from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question
from users.models import Profile
from django.http import HttpResponse
# Create your views here.


# class QuestionList(ListView):
#     model = Question
#     context_object_name = 'questions'
#     template_name = 'questions_list.html'


# class QuestionDetail(DetailView):
#     model = Question
#     template_name = 'question_detail.html'
#     context_object_name = 'question'
def questionListView(request):
    questions = Question.objects.all()
    userP = Profile.objects.get(user=request.user)
    # solved = False
    # for question_solved in user.questions_solved.all():
    #     if question_solved.id == question.id:
    #         solved = True
    #         print(solved, 'solved')

    context = {
        # 'solved': solved,
        'questions': questions,
        'userP': userP
    }
    return render(request, 'questions_list.html', context)


def questionDetailView(request, id):
    question = Question.objects.get(id=id)
    user = Profile.objects.get(user=request.user)
    solved = False
    for question_solved in user.questions_solved.all():
        if question_solved.id == question.id:
            solved = True
            print(solved, 'solved')

    context = {
        'solved': solved,
        'question': question
    }
    return render(request, 'question_detail.html', context)


def checkAnswer(request, id):
    question = Question.objects.get(id=id)
    ans_submitted = request.POST.get('ans')

    # print('you said =============', ans_submitted)
    if ans_submitted == question.answer_text:
        right = True
        if not request.user.is_anonymous:
            userP = Profile.objects.get(user=request.user)
            userP.problems_solvd += 1
            userP.questions_solved.add(question)
            userP.save()
        # print(userP.problems_solvd)

    else:
        right = False
    context = {'right': right}
    return render(request, 'ansercheck.html', context)
