from django.db import models
from django.utils import timezone

# Create your models here.

class Note (models.Model):
    alias = models.CharField(max_length = 255)
    note = models.CharField(max_length = 255)
    date_posted = models.DateField(default = timezone.now)
    state = (
        ('m', 'marked'),
        ('u', 'unmarked'),
    )
    status = models.CharField(max_length = 1, choices = state, default = 'u')

    def __str__(self):
        return self.alias