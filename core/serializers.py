from rest_framework import serializers

from .models import Tender

class TenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tender
        fields='__all__'