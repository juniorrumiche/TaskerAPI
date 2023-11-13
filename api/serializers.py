from rest_framework import serializers
from api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "completed"]


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
