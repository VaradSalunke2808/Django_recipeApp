from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    yop = models.IntegerField()
    contact = models.CharField(max_length=10)
    stream = models.CharField(max_length=10,default=None)


class Cars(models.Model):
    name = models.CharField(max_length=10)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.name