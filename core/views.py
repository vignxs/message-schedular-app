from django.shortcuts import render

from rest_framework import viewsets
from .models import MessageEvent
from .serializers import MessageEventSerializer


class MessageEventViewSet(viewsets.ModelViewSet):
    queryset = MessageEvent.objects.all()
    serializer_class = MessageEventSerializer
