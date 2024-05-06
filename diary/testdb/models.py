from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} (Subject id: {self.id})"
    
    class Meta:
        ordering = ["name"]
        # verbose_name_plural = "Subjects"


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    subjects = models.ManyToManyField(Subject)

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
    
    class Meta:
        ordering = ["name", "age"]
        # verbose_name_plural = "Teachers"


class Student(models.Model):
    name = models.CharField(max_length=80)
