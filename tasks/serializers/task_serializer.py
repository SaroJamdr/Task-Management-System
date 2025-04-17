from rest_framework import serializers
from ..models import Task
from datetime import date

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"title": "Title is required."})

        due_date = data.get('due_date')
        if due_date and due_date < date.today():
            raise serializers.ValidationError({"due_date": "Due date cannot be in the past."})
        return data
    
class TaskRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']