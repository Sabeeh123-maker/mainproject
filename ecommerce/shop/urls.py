from django.contrib import admin
from django.urls import path
from shop import views
app_name = 'shop'
urlpatterns = [
    path('products/<int:i>', views.ProductView.as_view(), name='product'),
    path('productdetail/<int:i>', views.ProductDetailView.as_view(), name='productdetail'),
    path('register', views.Registerview.as_view(), name='register'),
    path('login', views.Loginview.as_view(), name='login'),
    path('logout', views.Logoutview.as_view(), name='logout'),
    path('addcategory', views.AddCategory.as_view(), name='addcategory'),
    path('addproduct', views.AddProduct.as_view(), name='addproduct'),
    path('addstock/<int:i>', views.AddStock.as_view(), name='addstock'),
]