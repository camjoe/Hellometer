from rest_framework import serializers
from .models import VendorClients

class VendorClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorClients
        fields = '__all__'