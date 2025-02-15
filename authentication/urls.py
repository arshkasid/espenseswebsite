from .views import RegisterView, LoginView, UsernameValidateView, EmailValidateView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate-username/', csrf_exempt(UsernameValidateView.as_view()), name='validate-username'),
    path('validate-email/', csrf_exempt(EmailValidateView.as_view()), name='validate-email'),
]
