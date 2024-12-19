from django.urls import path
from .views import FlatListAPIView, FlatCreateAPIView, FlatDetailAPIView, FlatUpdateAPIView,FlatDeleteAPIView, SubscriptionListAPIView, SubscriptionDetailAPIView

urlpatterns = [
    path('flats/', FlatListAPIView.as_view(), name='flat-list'),  # Endpoint: /flats/
    path('flats/<str:flat_no>/', FlatDetailAPIView.as_view(), name='flat-detail'),
    path('flats/add/', FlatCreateAPIView.as_view(), name='flat-add'),  # POST to add a flat
    path('flats/<str:flat_no>/update/', FlatUpdateAPIView.as_view(), name='flat-update'),
    path('flats/<str:flat_no>/delete/', FlatDeleteAPIView.as_view(), name='flat-delete'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription-list'),  # Show all subscriptions
    path('subscriptions/<int:id>/', SubscriptionDetailAPIView.as_view(), name='subscription-detail'),  # Operations on a single subscription
]
