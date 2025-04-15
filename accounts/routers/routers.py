
from rest_framework .routers import DefaultRouter
from django.urls import path
from ..viewsets.user_viewset import RegisterView, UserProfileView
from ..viewsets.user_viewset import LoginView, RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# router = DefaultRouter()
# router.register('accounts', AccountViewSet, basename='accountsViewsets')

urlpatterns = [
    path('login/', LoginView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]