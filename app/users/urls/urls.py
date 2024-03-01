from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from ..views import CreateUserView, AllUserView, DeleteUserView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('create-users/', CreateUserView.as_view()),
    path('users/', AllUserView.as_view()),
    path('del-user/<int:pk>', DeleteUserView.as_view())
]
