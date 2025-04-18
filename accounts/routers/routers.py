from django.urls import path
from ..viewsets.user_viewset import RegisterView, UserProfileView
from ..viewsets.user_viewset import LoginView, RegisterView, UserProfileView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]