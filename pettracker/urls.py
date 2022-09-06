from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('pets/', views.PetList.as_view(), name='pet_list'),
    path('expenses/', views.ExpenseList.as_view(), name='expense_list'),
    path('observations/', views.ObservationList.as_view(), name='observation_list'),
    path('records/', views.RecordList.as_view(), name='record_list'),
    # DETAIL ROUTES
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('pets/<int:pk>', views.PetDetail.as_view(), name='pet_detail'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view(), name='expense_detail'),
    path('observations/<int:pk>', views.ObservationDetail.as_view(),
         name='observation_detail'),
    path('records/<int:pk>', views.RecordDetail.as_view(), name='record_detail'),
]
