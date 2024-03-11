from rest_framework import serializers
from .models import MessageEvent


class MessageEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MessageEvent
        fields = ['id', 'date', 'time', 'message']
