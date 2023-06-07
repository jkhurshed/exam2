from django.db import models


class Student(models.Model):

    name = models.CharField("Имя студента", max_length=100)
    surname = models.CharField("Фамилия студента", max_length=100)
    email = models.EmailField("Email студента")
    course = models.ManyToManyField("education.course")
    

    class Meta:
        ordering = ["surname"]
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self) -> str:
        return f"{self.surname} {self.name}"
