from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class BookingViewset(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    parser_classes = (MultiPartParser, FormParser)

class MenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
def get_permissions(self):
    if(self.request.method=='GET'):
        return []

    return [IsAuthenticated()]
#
#class CartViewset(viewsets.ModelViewSet):
#    serializer_class = CartSerializer
#    queryset = Cart.objects.all()
#
class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

#class OrderItemViewset(viewsets.ModelViewSet):
#    serializer_class = OrderItemSerializer
#    queryset = OrderItem.objects.all()
#