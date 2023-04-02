from django.shortcuts import redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator


User = get_user_model()


@method_decorator(ratelimit(key='ip', rate='100/m', block=True), name='dispatch')
@method_decorator(ratelimit(key='post:government_id', rate='100/m', block=True), name='dispatch')
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
        response.set_cookie('jwt', str(refresh.access_token), httponly=True)
        return redirect('login')


@method_decorator(ratelimit(key='ip', rate='100/m', block=True), name='dispatch')
@method_decorator(ratelimit(key='post:government_id', rate='100/m', block=True), name='dispatch')
class UserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        response = Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)

        # redirect to the /dashboard endpoint
        response.set_cookie('jwt', str(refresh.access_token), httponly=True)
        return redirect('dashboard')
