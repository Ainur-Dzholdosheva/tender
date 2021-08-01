from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TenderSerializer, BuyerSerializer, SellerSerializer, RedFlagSerializer
from .models import RedFlag, Tender, Buyer, Seller, RedFlag

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all().order_by('name')
    serializer_class = TenderSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all().order_by('name')
    serializer_class = BuyerSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all().order_by('name')
    serializer_class = SellerSerializer

class RedFlagViewSet(viewsets.ModelViewSet):
    queryset = RedFlag.objects.all().order_by('name')
    serializer_class = RedFlagSerializer