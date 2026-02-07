from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (
	TokenObtainPairSerializer,
	TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class TokenObtainPairResponseSerializer(serializers.Serializer):
	refresh = serializers.CharField()
	access = serializers.CharField()


class TokenRefreshResponseSerializer(serializers.Serializer):
	access = serializers.CharField()


class SwaggerTokenObtainPairView(TokenObtainPairView):
	@swagger_auto_schema(
		request_body=TokenObtainPairSerializer,
		responses={200: TokenObtainPairResponseSerializer},
	)
	def post(self, request: Request, *args, **kwargs) -> Response:
		return super().post(request, *args, **kwargs)


class SwaggerTokenRefreshView(TokenRefreshView):
	@swagger_auto_schema(
		request_body=TokenRefreshSerializer,
		responses={200: TokenRefreshResponseSerializer},
	)
	def post(self, request: Request, *args, **kwargs) -> Response:
		return super().post(request, *args, **kwargs)
