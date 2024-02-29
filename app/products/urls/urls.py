from django.urls import path
from ..views import CreateProductsView, GetAllProductsView, DeleteOneProductView, GetSingleProductView

urlpatterns = [
    path('crete-product/', CreateProductsView.as_view()),
    path("one-product/<int:pk>", GetSingleProductView.as_view()),
    path('all-products/', GetAllProductsView.as_view()),
    path('delete-product/<int:pk>', DeleteOneProductView.as_view())
]
