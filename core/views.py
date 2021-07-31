from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TenderSerializer
from .models import Tender

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all().order_by('name')
    serializer_class = TenderSerializer