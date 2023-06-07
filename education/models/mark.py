from django.db import models


class Mark(models.Model):

    value = models.IntegerField("Оценка")
    mark_date = models.DateTimeField("Transaction date", auto_now_add=True)
    course = models.ForeignKey("education.course", on_delete=models.CASCADE, 
                               verbose_name="Course", related_name="courses")
    student = models.ForeignKey("education.student", on_delete=models.CASCADE,
                               verbose_name="Student", related_name="students")
    
    class Meta:
        
        verbose_name = "Mark"
        verbose_name_plural = "Marks"
    
    def __str__(self) -> str:
        return str(self.value)