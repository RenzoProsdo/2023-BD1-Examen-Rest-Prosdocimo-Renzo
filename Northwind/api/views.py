from django.shortcuts import render
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import *
from api.models import *

#Customers
@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, customerid):
    try:
        customer = Customers.objects.get(customerid=customerid)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomersSerializer(customer, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomersSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Suppliers
@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier(request, supplierid):
    try:
        supplier = Suppliers.objects.get(supplierid=supplierid)
    except Suppliers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuppliersSerializer(supplier, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuppliersSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Categories
@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category(request, categoryid):
    try:
        category = Categories.objects.get(categoryid=categoryid)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriesSerializer(category, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriesSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Products
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product(request, productid):
    try:
        product = Products.objects.get(productid=productid)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Orders
@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order(request, orderid):
    try:
        order = Orders.objects.get(orderid=orderid)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrdersSerializer(order, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Orderdetails
@api_view(['GET', 'POST'])
def orderdetails(request):
    if request.method == 'GET':
        orderdetails = Orderdetails.objects.all()
        serializer = OrderDetailsSerializer(orderdetails, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderdetail(request, orderid):
    try:
        orderdetail = Orderdetails.objects.get(orderid=orderid)
    except Orderdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderDetailsSerializer(orderdetail, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderDetailsSerializer(orderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        orderdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Employees
@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, employeeid):
    try:
        employee = Employees.objects.get(employeeid=employeeid)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeesSerializer(employee, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Endpoints


@api_view(['GET'])
def endPoint1(request):
        supplierid = request.GET.get('supplierid')
        categoryid = request.GET.get('categoryid')
        stockMin = request.GET.get('stockmin')

        try:
            suppliers = Suppliers.objects.get(supplierid=supplierid)
            category = Categories.objects.get(categoriesid=categoryid)
        except (Suppliers.DoesNotExist, Categories.DoesNotExist):
            return Response({'error': 'Proveedor y/o categoría no existentes'}, status=404)

        products = Product.objects.filter(
            suppliers=suppliers,
            categories=categories,
            discontinued=False
        ).annotate(
            stockFuturo=ExpressionWrapper(F('unitsinstock') + F('unitsonorder'),
        output_field=fields.IntegerField())
        ).filter(stockFuturo__lt=stock_min).order_by('stockFuturo')

        if not products.exists():
            return Response({'message': 'No hay productos'}, status=204)

        response_data = []
        for product in products:
            response_data.append({
                'ProductId': product.productid,
                'ProductName': product.productname,
                'StockFuturo': product.stock_futuro,
                'UnitPrice': float(product.unitprice),  
      })

        return Response(response_data, safe=False, status=200)



