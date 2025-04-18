from rest_framework import serializers
from ..models import Task
from datetime import date

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'status', 'assigned_to')
    
class TaskRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
    fields = ['id', 'title', 'description', 'due_date', 'status', 'assigned_to']

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'assigned_to']

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']