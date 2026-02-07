from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignupSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, min_length=8)

	class Meta:
		model = get_user_model()
		fields = ["username", "password"]

	def create(self, validated_data):
		user_model = get_user_model()
		return user_model.objects.create_user(
			username=validated_data["username"],
			password=validated_data["password"],
		)


class LogoutSerializer(serializers.Serializer):
	refresh = serializers.CharField(write_only=True)

	def save(self, **kwargs):
		refresh_token = self.validated_data["refresh"]
		token = RefreshToken(refresh_token)
		token.blacklist()

