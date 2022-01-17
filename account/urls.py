from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ChangePasswordView, ForgotPassword, ForgotPasswordComplete, SignupView, ActivationView

urlpatterns = [
    # path('', views.HiAuthView.as_view(), name='hi_auth'),
    path('signup/', SignupView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api/change-password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPassword.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplete.as_view()),
]