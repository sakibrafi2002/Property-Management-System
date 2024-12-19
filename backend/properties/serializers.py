from rest_framework import serializers
from .models import Flat, Subscription


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'  # Include all fields from the Flat model


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'  # Include all fields from the Subscription model