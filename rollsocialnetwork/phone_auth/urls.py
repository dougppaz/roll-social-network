"""
phone auth urls
"""
from django.urls import path
from .views import (
    LoginView,
    RequestVerificationCodeView,
    VerifyVerificationCodeView,
    VerifyOTPCodeView,
    ShowOTPSecretView,
)

urlpatterns = [
    path("login/",
         LoginView.as_view(),
         name="phone-auth-login"),
    path("request/<str:phone_number>/",
         RequestVerificationCodeView.as_view(),
         name="request-verification-code"),
    path("verify/<str:phone_number>/",
         VerifyVerificationCodeView.as_view(),
         name="verify-verification-code"),
    path("verify-otp/<str:phone_number>/",
         VerifyOTPCodeView.as_view(),
         name="verify-otp-code"),
    path("show-otp-secret/", ShowOTPSecretView.as_view()),
]
