from django.shortcuts import render
from .models import Recipe, RecipeSteps
from .serializers import RecipeSerializer, RecipeStepsSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status


class RecipeSharedView(APIView):
    @swagger_auto_schema(
        operation_description="공유된 모든 레시피를 조회합니다.",
        responses={
            200: RecipeSerializer(many=True),
        }
    )
    def get(self, request):
        shared_recipes = Recipe.objects.filter(is_shared=True)
        serializer = RecipeSerializer(shared_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecipeSharedDetailView(APIView):

    @swagger_auto_schema(
        operation_description="공유된 레시피 중 하나를 선택하여 조회합니다.",
        responses={
            200: RecipeSerializer,
            404: 'Not Found'
        }
    )
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk, is_shared=True)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class RecipeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="로그인한 유저의 모든 레시피를 조회합니다.",
        responses={
            200: RecipeSerializer(many=True),
            201: RecipeSerializer,
            400: 'Bad Request'
        }
    )
    def get(self, request):
        recipes = Recipe.objects.filter(user_id=request.user)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="새로운 레시피 생성.",
        request_body=RecipeSerializer,
        responses={
            201: RecipeSerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="레시피 부분 수정.",
        request_body=RecipeSerializer,
        responses={
            200: RecipeSerializer,
            400: 'Bad Request'
        }
    )
    def patch(self, request):
        serializer = RecipeSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="레시피의 상세 사항을 조회합니다.",
        responses={
            200: RecipeSerializer, 
            204: 'No Content',
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk, user_id=request.user)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="특정 레시피를 업데이트 합니다.",
        request_body=RecipeSerializer,
        responses={
            200: RecipeSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk, user_id=request.user)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="특정 레시피를 삭제합니다.",
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk, user_id=request.user)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class RecipeStepView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="특정 레시피의 모든 단계를 조회합니다.",
        responses={
            200: RecipeStepsSerializer(many=True),
        }
    )
    def get(self, request, recipe_pk):
        steps = RecipeSteps.objects.filter(recipe_id=recipe_pk)
        serializer = RecipeStepsSerializer(steps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
class RecipeStepDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="특정 레시피의 특정 단계를 조회합니다.",
        responses={
            200: RecipeStepsSerializer,
            404: 'Not Found'
        }
    )
    def get(self, request, recipe_pk, step_pk):
        try:
            step = RecipeSteps.objects.get(pk=step_pk, recipe_id=recipe_pk)
        except RecipeSteps.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeStepsSerializer(step)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(
        operation_description="특정 레시피의 특정 단계를 수정합니다.",
        request_body=RecipeStepsSerializer,
        responses={
            200: RecipeStepsSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def put(self, request, recipe_pk, step_pk):
        try:
            step = RecipeSteps.objects.get(pk=step_pk, recipe_id=recipe_pk)
        except RecipeSteps.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeStepsSerializer(step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="특정 레시피의 특정 단계를 부분 수정합니다.",
        request_body=RecipeStepsSerializer,
        responses={
            200: RecipeStepsSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def patch(self, request, recipe_pk, step_pk):
        try:
            step = RecipeSteps.objects.get(pk=step_pk, recipe_id=recipe_pk)
        except RecipeSteps.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeStepsSerializer(step, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="특정 레시피의 특정 단계를 삭제합니다.",
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, recipe_pk, step_pk):
        try:
            step = RecipeSteps.objects.get(pk=step_pk, recipe_id=recipe_pk)
        except RecipeSteps.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)