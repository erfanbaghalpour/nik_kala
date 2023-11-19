from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail')
]
