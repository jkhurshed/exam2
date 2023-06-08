from rest_framework.serializers import ModelSerializer

from ..models import Mark

class MarkSerializer(ModelSerializer):

    class Meta:
        model = Mark
        fields = ["id", "value", "mark_date", "course", "student"]