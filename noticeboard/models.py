from django.db import models


# Create your models here.
class Notice(models.Model):
    datetime_of_creation = models.DateTimeField(verbose_name='Created on', auto_now=True)
    title = models.CharField(verbose_name='Title', max_length=30)
    description = models.TextField()
    active = models.BooleanField(verbose_name='The notice is active')
    pin = models.BooleanField(verbose_name='The notice is pinned')

    def __str__(self):
        return self.title
