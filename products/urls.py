from django.urls import path
from .views import ProductListCreateView, ProductDetailView, OrderListCreateView, OrderDetailView

urlpatterns = [
    # URL-шляхи для продуктів
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # URL-шляхи для замовлень
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]