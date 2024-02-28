
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.users.urls.urls')),
    path('api/v1/', include('app.products.urls.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
