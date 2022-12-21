from django.db import models


# Create your models here.
class Task(models.Model):
    task1=models.CharField(max_length=50)
    priority1=models.IntegerField()
    date1=models.DateField()
    def __str__(self):
        return self.task1
