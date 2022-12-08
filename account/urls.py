from django.urls import path
from . import views

urlpatterns = [
    #   path('', views.home, name='home')
    path('products/', views.getProducts, name='products'),
    path('product/<str:pk>', views.getProduct, name='product'),

    path('product/update/<str:pk>', views.updateProduct, name='update-product'),
    path('product/<str:pk>/update', views.updateBoolean, name='update-boolean'),

    path('customer/', views.getCustomer, name='customer')
]