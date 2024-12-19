from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flat, Subscription
from .serializers import FlatSerializer, SubscriptionSerializer

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
            
            
            
class FlatDeleteAPIView(APIView):
    def delete(self, request, flat_no):
        try:
            flat = Flat.objects.get(flat_no=flat_no)  # Fetch the flat by primary key
            flat.delete()  # Delete the flat from the database
            return Response(
                {"message": f"Flat with flat_no '{flat_no}' has been deleted."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Flat.DoesNotExist:
            return Response(
                {"error": "Flat not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            

# class SubscriptionListAPIView(ListAPIView):
#     # Show All Subscriptions
#     queryset = Subscription.objects.all() 
#     serializer_class = SubscriptionSerializer
    
    
class SubscriptionListAPIView(APIView):
    # Show All Subscriptions
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create Subscription (POST)
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubscriptionDetailAPIView(APIView):
    # Show Subscription (GET)
    def get(self, request, id):
        try:
            subscription = Subscription.objects.get(id=id)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        
    

    # Update Subscription (PUT/PATCH)
    def put(self, request, id):
        try:
            subscription = Subscription.objects.get(id=id)
            serializer = SubscriptionSerializer(subscription, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            subscription = Subscription.objects.get(id=id)
            serializer = SubscriptionSerializer(subscription, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)

    # Delete Subscription (DELETE)
    def delete(self, request, id):
        try:
            subscription = Subscription.objects.get(id=id)
            subscription.delete()
            return Response({"message": f"Subscription with id '{id}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)