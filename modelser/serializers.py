from .models import students
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
