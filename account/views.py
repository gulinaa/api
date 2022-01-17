from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from .models import MyUser
from .celery import send_reset_code


class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully signed up!', status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Congratulation! Now your account successfully activated!', status=status.HTTP_200_OK)


class ForgotPassword(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        user = get_object_or_404(MyUser, email=email)
        user.is_active = False
        user.create_activation_code()
        user.save()
        send_reset_code.delay(email=user.email, activation_code=user.activation_code)
        return Response('Message has been sent', status=200)


class ForgotPasswordComplete(APIView):

    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Your password successfully reset!', status=200)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = MyUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Incorrect password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))

            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Your password successfully renewed',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

