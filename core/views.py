from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TenderSerializer, BuyerSerializer
from .models import Tender, Buyer

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all().order_by('name')
    serializer_class = TenderSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all().order_by('name')
    serializer_class = BuyerSerializer