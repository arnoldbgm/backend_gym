from django.urls import path
from ..views import CreateProductsView

urlpatterns = [
    path('crete-product/', CreateProductsView.as_view()),
]