from django.contrib import admin
from .models import Student, Course, Mark

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ("id", "name", "surname", "email", "display_courses")
    list_display_links = ("name", )

    def display_courses(self, obj):
        return ", ".join([course.title for course in obj.course.all()])

    display_courses.short_description = 'Courses'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ("id", "title", "description", "duration")
    list_display_links = ("title", )


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    model = Mark
    list_display = ("value", "mark_date", "course", "student")
    list_display_links = ("student",)