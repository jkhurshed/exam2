from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..serializers import StudentSerializer
from ..models import Student


class StudentViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'patch', 'post']