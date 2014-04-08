from django.db import models
from django.contrib.auth.models import User


class Bunk(models.Model):
    from_user = models.ForeignKey(User, related_name='bunk_from_user')
    to_user = models.ForeignKey(User, related_name='bunk_to_user')
    time = models.DateTimeField('bunk time')

    def __unicode__(self):
        return ('From ' + self.from_user.username +
                ' to ' + self.to_user.username)


class UserProfile(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    photo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username