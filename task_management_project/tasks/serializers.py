from rest_framework import serializers
from .models import User, Task


# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']


# Serializer for Task model with validation for assigned_to
class TaskSerializer(serializers.ModelSerializer):
    # String representation of the assigned user for readability
    #assigned_to = serializers.StringRelatedField(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.values_list('username'), source='assigned_to', write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'assigned_to_id', 'created_at']


    # Custom validation to ensure the assigned user exists
    def validate_assigned_to(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Assigned user does not exist.")
        return value
