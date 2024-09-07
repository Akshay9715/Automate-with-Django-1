from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Uploads(models.Model):
    file = models.FileField(upload_to='uploads/')
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name