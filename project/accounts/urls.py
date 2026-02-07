from django.urls import path

from .jwt_views import SwaggerTokenObtainPairView, SwaggerTokenRefreshView

from .views import SignupView, LogoutView

urlpatterns = [
	path("token/", SwaggerTokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("token/refresh/", SwaggerTokenRefreshView.as_view(), name="token_refresh"),
	path("signup/", SignupView.as_view(), name="signup"),
	path("logout/", LogoutView.as_view(), name="logout"),
]