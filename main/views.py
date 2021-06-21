from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import *
from main.serializers import *


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
