from django.db import models
from rest_framework import fields, serializers
from .models import Todo

# 
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')