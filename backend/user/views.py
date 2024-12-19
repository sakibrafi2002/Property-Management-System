from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser  # For authentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# CRUD Views for the User model
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, nid):
        try:
            user = User.objects.get(nid=nid)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, nid):
        try:
            user = User.objects.get(nid=nid)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, nid):
            try:
                user = User.objects.get(nid=nid)
                serializer = UserSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, nid):
        try:
            user = User.objects.get(nid=nid)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# # Authentication Views
# @api_view(['POST'])
# def register(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if username and password:
#         user = AuthUser.objects.create_user(username=username, password=password)
#         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#     return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user:
#         login(request, user)
#         return Response({'message': 'Logged in successfully'})
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     return Response({'message': 'Logged out successfully'})
