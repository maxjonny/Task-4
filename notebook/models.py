from django.db import models
from django.utils import timezone as tz


class Notebook(models.Model):
    header = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=200)
    date_of_completion = models.DateField()
    status_type = [
        (0, 'выполняется'),
        (1, 'выполнено'),
    ]
    status = models.IntegerField(choices=status_type, default=0)

    def __str__(self):
        return self.header
