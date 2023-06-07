from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..serializers import CourseSerializer
from ..models import Course


class CourseViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'patch', 'post']