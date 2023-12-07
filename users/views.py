from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class HomePage(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return Response({"Message": "Home Page"})


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        new_data = UserRegistrationSerializer(data=request.data)
        new_data.is_valid(raise_exception=True)
        new_data.save()
        return Response({"Success": "Thanks for signing up"}, status=status.HTTP_201_CREATED)



