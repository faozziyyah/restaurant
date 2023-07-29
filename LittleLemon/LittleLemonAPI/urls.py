from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewset)
router.register('menu_items', MenuItemViewset)
router.register('carts', CartViewset)
router.register('orders', OrderViewset)
router.register('order_items', OrderItemViewset)

urlpatterns = [
    path('', include(router.urls)),
]