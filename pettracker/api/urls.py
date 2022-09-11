from django.urls import path
from django.conf.urls import include
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # path('users/', views.UserList.as_view(), name='user_list'),
    path('pets/', views.PetList.as_view(), name='pet-list'),
    path('expenses/', views.ExpenseList.as_view(), name='expense-list'),
    path('observations/', views.ObservationList.as_view(), name='observation-list'),
    path('records/', views.RecordList.as_view(), name='record-list'),

    # DETAIL ROUTES
    # path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('pets/<int:pk>', views.PetDetail.as_view(), name='pet-detail'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view(), name='expense-detail'),
    path('observations/<int:pk>', views.ObservationDetail.as_view(),
         name='observation-detail'),
    path('records/<int:pk>', views.RecordDetail.as_view(), name='record-detail'),

    # urls that wire the views which allow us to obtain and refresh JWT tokens
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
