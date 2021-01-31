from django.urls import path, include
from .views import LogoutAPIView, LoginAPIView, UserViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserViewSet)
app_name = "users"

urlpatterns = [
    path('profile/', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
