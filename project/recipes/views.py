from django.shortcuts import render
from .models import Recipe, RecipeSteps
from .serializers import RecipeSerializer, RecipeStepsSerializer
from rest_framework import viewsets
from rest_framewor.views import APIView
from rest_framework.response import Response


# Create your views here.
class RecipeAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
