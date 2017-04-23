from django.db import models
from django.contrib.auth.models import Group, AbstractUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    pass


class Pomodoro(models.Model):
    user = models.ForeignKey(User, null=False, related_name='pomodoros', on_delete=models.CASCADE)
    started = models.DateTimeField(default=timezone.now())
    is_canceled = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = ('user','started')
        ordering = ('started',)

    def __unicode__(self):
        return '#{} {}'.format(self.id_user, self.started)