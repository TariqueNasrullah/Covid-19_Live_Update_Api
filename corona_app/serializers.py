from rest_framework import serializers
from .models import CoronaData, CountryData

class CoronaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaData
        fields = [
            'total_case', 
            'death', 
            'recovered', 
            'active', 
            'closed',
            'mild',
            'mild_percentage',
            'serious',
            'serious_percentage',
            'recovered_or_discharged',
            'recovered_or_discharged_percentage',
            'death_percentage',
        ]

class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryData
        fields = '__all__'