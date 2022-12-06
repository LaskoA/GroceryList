from django.urls import path
from . import views
from .views import (
    CategoryListView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryCreateView,
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    PurchaseListView,
    PurchaseCreateView,
    PurchaseDeleteView,
    PurchaseDetailView,
    PurchaseUpdateView,
    change_status,
)

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("purchases/", PurchaseListView.as_view(), name="purchase-list"),
    path("purchases/<int:pk>/", PurchaseDetailView.as_view(), name="purchase-detail"),
    path("purchases/create", PurchaseCreateView.as_view(), name="purchase-create"),
    path("purchases/<int:pk>/update/", PurchaseUpdateView.as_view(), name="purchase-update"),
    path("purchases/<int:pk>/delete/", PurchaseDeleteView.as_view(), name="purchase-delete"),
    path("purchases/<int:pk>/change-status", change_status, name="change-status"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
]
