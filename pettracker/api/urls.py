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
    path('user/', include(('accounts.urls', 'accounts'), namespace='users')),

    # path('users/', views.UserList.as_view(), name='user_list'),
    path('pets/', views.PetList.as_view(), name='pet_list'),
    path('expenses/', views.ExpenseList.as_view(), name='expense_list'),
    path('observations/', views.ObservationList.as_view(), name='observation_list'),
    path('records/', views.RecordList.as_view(), name='record_list'),

    # DETAIL ROUTES
    # path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('pets/<int:pk>', views.PetDetail.as_view(), name='pet_detail'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view(), name='expense_detail'),
    path('observations/<int:pk>', views.ObservationDetail.as_view(),
         name='observation_detail'),
    path('records/<int:pk>', views.RecordDetail.as_view(), name='record_detail'),

    # urls that wire the views which allow us to obtain and refresh JWT tokens
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
