from django.contrib import admin 
from django.urls import path, include
#from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register('booking', BookingViewset)
router.register('menu-items', MenuItemViewset)
router.register('categories', CategoryViewset)
router.register('ratings', RatingsView)
router.register('cart/menu-items', CartViewset)
router.register('orders', OrderViewset)
  
urlpatterns = [ 
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]