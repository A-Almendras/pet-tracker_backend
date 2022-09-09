from django.urls import path
from .views import CreateNewUserView

urlpatterns = [
    path('register', CreateNewUserView.as_view(), name='create_user')
]
