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


class House(models.Model):
    name = models.CharField(max_length=50)
    founder = models.CharField(max_length=80)
    emblem = models.CharField(max_length=50)
    head = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    subjects = models.ManyToManyField(Subject)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_students")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} of {self.house}"

    class Meta:
        ordering = ["first_name", "last_name", "house"]
