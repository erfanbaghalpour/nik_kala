from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>/', views.product_detail, name='product_detail')
]
