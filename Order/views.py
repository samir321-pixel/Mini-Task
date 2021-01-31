from rest_framework.permissions import IsAuthenticated
from .models import Review, Product, OrderDetail, Mediators
from .serializers import (
    OrderDetailSerializer, ProductSerializer, ReviewSerializer, MediatorSerializer
)
from rest_framework import viewsets



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return OrderDetail.objects.all()

    def perform_create(self, serializer):
        serializer = OrderDetailSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer = ProductSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()


class MediatorViewSet(viewsets.ModelViewSet):
    serializer_class = MediatorSerializer

    def get_queryset(self):
        return Mediators.objects.all()

    def perform_create(self, serializer):
        serializer = MediatorSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer = ReviewSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
