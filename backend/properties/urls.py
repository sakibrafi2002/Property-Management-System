from django.urls import path
from .views import FlatListAPIView, FlatCreateAPIView

urlpatterns = [
    path('flats/', FlatListAPIView.as_view(), name='flat-list'),  # Endpoint: /flats/
    path('flats/add/', FlatCreateAPIView.as_view(), name='flat-add'),  # POST to add a flat
]
