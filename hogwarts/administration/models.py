from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        ordering = ["subject",]
    
    def __str__(self) -> str:
        return f"{self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    subjects = models.ManyToManyField(Subject)

    class Meta:
        ordering = ["name", "-age"]

    def __str__(self) -> str:
        return f"{self.name}"


class House(models.Model):
    name = models.CharField(max_length=64)
    founder = models.CharField(max_length=64)
    emblem = models.CharField(max_length=64)
    head = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name",]
    
    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=80)
    subjects = models.ManyToManyField(Subject)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="students_of_house")

    class Meta:
        ordering = ["name",]
    
    def __str__(self) -> str:
        return f"{self.name}"
