from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    parser_classes = (MultiPartParser, FormParser)

class MenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
def get_permissions(self):
    if(self.request.method=='GET'):
        return []

    return [IsAuthenticated()]

class CartViewset(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderItemViewset(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
