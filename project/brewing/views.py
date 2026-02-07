from .models import BrewingHistory
from .serializers import BrewingHistorySerializer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BrewingHistoryView(generics.ListCreateAPIView):
    serializer_class = BrewingHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BrewingHistory.objects.filter(user_id=self.request.user)

    @swagger_auto_schema(
        operation_description="로그인한 유저의 모든 브루잉 히스토리를 조회합니다.",
        responses={
            200: BrewingHistorySerializer(many=True),
            400: 'Bad Request'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="새로운 브루잉 히스토리 생성.",
        request_body=BrewingHistorySerializer,
        responses={
            201: BrewingHistorySerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request, *args, **kwargs):
        if 'recipe_id' not in request.data:
            return Response(
                {'recipe_id': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BrewingHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrewingHistorySerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'history_id'

    def get_queryset(self):
        return BrewingHistory.objects.filter(user_id=self.request.user)
    @swagger_auto_schema(
        operation_description="특정 브루잉 히스토리의 상세 사항을 조회합니다.",
        responses={
            200: BrewingHistorySerializer,
            404: 'Not Found'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="특정 브루잉 히스토리를 삭제합니다.",
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)