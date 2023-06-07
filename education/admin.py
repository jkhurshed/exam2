from django.contrib import admin
from .models import Student, Course, Mark

'''@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ("id", "name", "surname", "email", "course", "mark")
    list_display_links = ("name", )
'''

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Mark)