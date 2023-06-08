from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..serializers import MarkSerializer
from ..models import Mark


class MarkViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    http_method_names = ['get', 'patch', 'post']