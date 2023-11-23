from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('customers/', views.customers),
    path('supliers/', views.suppliers),
    path('categories/',views.categories),
    path('products/',views.products),
    path('orders/',views.orders),
    path('orderdetails/',views.orderdetail),
    path('employees/',views.employees),
    path('endPoint1/',views.endPoint1)

]

