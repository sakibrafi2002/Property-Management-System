from rest_framework import serializers
from .models import Flat

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'  # Include all fields from the Flat model
