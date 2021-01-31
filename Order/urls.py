from rest_framework import routers
from django.urls import path, include

from .views import OrderViewSet, ReviewViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('order_view', OrderViewSet, 'order_view')
router.register('review_view', ReviewViewSet, 'review_view')
router.register('product_view', ProductViewSet, 'product_view')
urlpatterns = [
    path(r'', include(router.urls)),
]
