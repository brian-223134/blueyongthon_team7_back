from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SignupView, LogoutView

urlpatterns = [
	path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
	path("signup/", SignupView.as_view(), name="signup"),
	path("logout/", LogoutView.as_view(), name="logout"),
]