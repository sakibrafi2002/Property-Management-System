from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flat
from .serializers import FlatSerializer

class FlatListAPIView(ListAPIView):
    queryset = Flat.objects.all()  # Fetch all flats
    serializer_class = FlatSerializer  # Use the FlatSerializer

class FlatCreateAPIView(APIView):
    def post(self, request):
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the flat instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)