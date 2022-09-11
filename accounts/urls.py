from django.urls import path
from .views import CreateUserView, UserList, UserDetail

urlpatterns = [
    path('register', CreateUserView.as_view(), name='create_user'),
    path('users', UserList.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>',
         UserDetail.as_view({'get': 'list'}), name='user-detail'),
]
