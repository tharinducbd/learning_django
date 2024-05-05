from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    subject = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"


class Student(models.Model):
    name = models.CharField(max_length=80)
