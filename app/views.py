from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer,CategorySerializer

from .models import Category,Product


@api_view(http_method_names=['POST','GET'])
def product_list_create_api_view(request):
    if request.method=='GET':
        products=Product.objects.all()
        serializer=ProductSerializer(instance=products,many=True)
        return Response(serializer.data,status=200)

    if request.method=='POST':
        received_data=request.data
        serializer=ProductSerializer(data=received_data)

        if serializer.is_valid():
            product=serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


@api_view(http_method_names=['POST','GET'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        received_data = request.data
        serializer = CategorySerializer(data=received_data)

        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


