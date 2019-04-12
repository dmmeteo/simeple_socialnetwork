from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like')
    unlike = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='unlike')
    release_date = models.DateField(auto_now_add=True)

    @property
    def sum_likes(self):
        return self.like.count()

    @property
    def sum_unlikes(self):
        return self.unlike.count()

