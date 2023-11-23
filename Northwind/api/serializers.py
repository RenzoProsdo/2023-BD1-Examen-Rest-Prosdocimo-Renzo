from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

#Employees
class ReportsToSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    reportsto = ReportsToSerializer(many=False)
    class Meta:
        model = Employees
        fields = '__all__'

#Customers
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

#Suppliers
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

#Categories
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

# Products
class ProductsSerializer(serializers.ModelSerializer):
    categoryid = CategoriesSerializer(many=False)
    supplierid = SuppliersSerializer(many=False)
    class Meta:
        model = Products
        fields = '__all__'

#Order Details
class OrderDetailsSerializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many=False)
    class Meta:
        model = Orderdetails
        fields = '__all__'


#Orders
class OrdersSerializer(serializers.ModelSerializer):
    customerid = CustomersSerializer(many=False)
    employeeid = EmployeesSerializer(many=False)
    shipvia = SuppliersSerializer(many=False)
    class Meta:
        model = Orders
        fields = '__all__'


