#accounts/urls.py

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = 'accounts'
urlpatterns = [
    path('', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    # path('<str:username>/', views.profile, name="profile"),
]