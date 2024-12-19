from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    # User CRUD
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<str:nid>/', UserDetailView.as_view(), name='user-detail'),
    
    # # Authentication
    # path('auth/register/', register, name='register'),
    # path('auth/login/', login_view, name='login'),
    # path('auth/logout/', logout_view, name='logout'),
]