from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    subject = models.CharField(max_length=80)
    # subject_link = models.ForeignKey(Subject,
    #                                  on_delete=models.CASCADE,
    #                                  related_name="Teachers")

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"


class Student(models.Model):
    name = models.CharField(max_length=80)
