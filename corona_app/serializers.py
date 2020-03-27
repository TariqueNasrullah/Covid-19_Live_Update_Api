from rest_framework import serializers
from .models import CoronaData, CountryData, DateCaseData, DateDeathData

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

class DateCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateCaseData
        fields = '__all__'

class DateDeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateDeathData
        fields = '__all__'