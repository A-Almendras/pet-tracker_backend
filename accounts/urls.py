from django.urls import path
from .views import CreateUserView, UserList, UserDetail

urlpatterns = [
    path('register-user', CreateUserView.as_view(), name='create_user'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
