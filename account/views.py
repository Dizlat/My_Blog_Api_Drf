from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import *
#TODO: register View


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Successfully signed up", status=status.HTTP_201_CREATED)



#TODO: activate view
#TODO: login view
#TODO: logout view