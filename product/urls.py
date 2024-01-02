from django.urls import path, include
from . import views
from .views import ProductDetailView

urlpatterns = [
    # path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('product_detail/<slug>/', ProductDetailView.as_view(), name='product_detail'),
]
