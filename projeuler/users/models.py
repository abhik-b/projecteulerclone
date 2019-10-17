from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problems_solvd = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
