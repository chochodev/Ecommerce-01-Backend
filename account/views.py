from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

# PRODUCT VIEW
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateBoolean(request, pk):
    data = request.data
    product = Product.objects.get(id=pk)
    
    serializer = BooleanSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# CUSTOMER VIEW
@api_view(['GET'])
def getCustomer(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)