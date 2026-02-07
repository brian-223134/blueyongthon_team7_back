from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import SignupSerializer, LogoutSerializer


class SignupView(generics.CreateAPIView):
	serializer_class = SignupSerializer
	permission_classes = [permissions.AllowAny]


class LogoutView(generics.GenericAPIView):
	serializer_class = LogoutSerializer
	permission_classes = [permissions.AllowAny]

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(status=status.HTTP_204_NO_CONTENT)

