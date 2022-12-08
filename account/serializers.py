from rest_framework import serializers 
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BooleanSerializer(serializers.ModelSerializer):
    wishlist = serializers.BooleanField(required=False)
    cartlist = serializers.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ['wishlist', 'cartlist']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'