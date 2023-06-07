from django.db import models


class Course(models.Model):

    title = models.CharField("Название курса", max_length=150)
    description = models.CharField("Описание курса", max_length=250, blank=True)
    duration = models.DurationField("Длительность", max_length=100)

    class Meta:
        ordering = ["title"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
    def __str__(self) -> str:
        return self.title
    