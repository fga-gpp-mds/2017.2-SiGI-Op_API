from .models import TechnicalReserve
from rest_framework import serializers

class TechnicalReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalReserve
        fields = [
            'id',
            'length',
            'latitude',
            'longitude',
            'infrastructure',
        ]