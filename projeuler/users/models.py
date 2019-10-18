from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from questions.models import Question


class Achievement(models.Model):
    title = models.CharField(max_length=120)
    question_solvd_to_get = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problems_solvd = models.IntegerField(default=0)
    questions_solved = models.ManyToManyField(Question)
    achivements = models.ManyToManyField(Achievement, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def qcount(self):

        return Question.objects.count()

    def progress(self):
        qcount = Question.objects.count()
        return (self.problems_solvd/qcount)*100

    def achievments_completed(self):
        for a in Achievement.objects.all():
            if self.problems_solvd == a.question_solvd_to_get:
                self.achivements.add(a)

        return self.achivements.all()


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


# for i in a.questions_solved.all():
#     print('q----', i.question_text)
#     # print('--q',q)
#     if i.id==1:
#         print('match founs')
#     else:
#         'not matched'
