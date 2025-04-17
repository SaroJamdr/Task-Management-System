from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from ..models import CustomUser
from rest_framework.permissions import IsAuthenticated
from ..serializers.user_serializer import RegisterSerializer, LoginSerializer, ProfileSerializer, UserSerializer

class RegisterView(APIView):
    queryset= CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = RegisterSerializer(user).data
        response_data = {
        'user': user_data,
        'token': str(refresh)
    }
        return Response(response_data, status=status.HTTP_201_CREATED)
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer= ProfileSerializer(request.user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    class_serializer= LoginSerializer
    permission_classes= [AllowAny]
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username_or_email= request.data.get('email')
        password= request.data.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            if user.is_active == False:
                return Response({'error': 'Account is inactive'}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            refresh= RefreshToken.for_user(user)
            refresh['remamber_me']= request.data.get('remember_me', False)
            user_obj= LoginSerializer(request.user, context={'request':request})
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_obj.data,
                'message': 'Logged in successfully',

                }, status=status.HTTP_200_OK)
        else:
            from django.db.models import Q
            user_obj = CustomUser.objects.filter(Q(email=username_or_email) | Q(username=username_or_email))
            if user_obj.exists():
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Invalid username/email'}, status=status.HTTP_401_UNAUTHORIZED)
            
