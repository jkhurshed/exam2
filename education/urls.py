from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, StudentViewSet, MarkViewSet

router = routers.DefaultRouter()
router.register("course", CourseViewSet, "course")
router.register("student", StudentViewSet, "student")
router.register("mark", MarkViewSet, "mark")

urlpatterns = [
    path('', include(router.urls))
]