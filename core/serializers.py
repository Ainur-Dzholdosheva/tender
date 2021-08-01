from rest_framework import serializers

from .models import Tender, Buyer, Seller, RedFlag

class TenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tender
        fields='__all__'

class BuyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Buyer
        fields='__all__'

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Seller
        fields='__all__'

class RedFlagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=RedFlag
        fields='__all__'