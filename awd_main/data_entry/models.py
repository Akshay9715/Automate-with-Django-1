from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
