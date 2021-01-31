from rest_framework import serializers
from .models import Review, Product, OrderDetail, Mediators


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MediatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediators
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
