# hostel/views.py

from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# hostel/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
