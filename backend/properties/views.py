from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flat
from .serializers import FlatSerializer

class FlatListAPIView(ListAPIView):
    queryset = Flat.objects.all()  # Fetch all flats
    serializer_class = FlatSerializer  # Use the FlatSerializer
    
class FlatDetailAPIView(APIView):
    def get(self, request, flat_no):
        try:
            flat = Flat.objects.get(flat_no=flat_no)  # Fetch the flat by primary key
            serializer = FlatSerializer(flat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Flat.DoesNotExist:
            return Response(
                {"error": "Flat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class FlatCreateAPIView(APIView):
    def post(self, request):
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the flat instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FlatUpdateAPIView(APIView):
    def put(self, request, flat_no):
        try:
            flat = Flat.objects.get(flat_no=flat_no)  # Fetch the flat by primary key
            serializer = FlatSerializer(flat, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Update the flat in the database
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Flat.DoesNotExist:
            return Response(
                {"error": "Flat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, flat_no):
        try:
            flat = Flat.objects.get(flat_no=flat_no)  # Fetch the flat by primary key
            serializer = FlatSerializer(flat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  # Partially update the flat in the database
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Flat.DoesNotExist:
            return Response(
                {"error": "Flat not found."},
                status=status.HTTP_404_NOT_FOUND
            )