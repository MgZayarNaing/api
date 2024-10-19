from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from ..models import *
from ..serializers import *
from django.http import JsonResponse

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_list(request):
    categories = Categories.objects.all().order_by("-id")
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_create(request):
    serializer = CategoriesSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_detail(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializer = CategoriesSerializer(category)
    return Response(serializer.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_update(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializer = CategoriesSerializer(category, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_delete(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return Response({"detail": "Category deleted successfully."}, status=status.HTTP_200_OK)