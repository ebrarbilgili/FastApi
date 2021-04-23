from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class UserModelView(APIView):
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
