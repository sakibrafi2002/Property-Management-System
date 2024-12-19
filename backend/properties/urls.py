from django.urls import path
from .views import FlatListAPIView, FlatCreateAPIView, FlatDetailAPIView, FlatUpdateAPIView

urlpatterns = [
    path('flats/', FlatListAPIView.as_view(), name='flat-list'),  # Endpoint: /flats/
    path('flats/<str:flat_no>/', FlatDetailAPIView.as_view(), name='flat-detail'),
    path('flats/add/', FlatCreateAPIView.as_view(), name='flat-add'),  # POST to add a flat
    path('flats/<str:flat_no>/update/', FlatUpdateAPIView.as_view(), name='flat-update'),
]
