from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .products import products
from .serializers import ProductSerializer

# Create your views here.




def getHomeRoute(request):
	return JsonResponse("Hello Home Page", safe=False)
	
@api_view(['GET'])
def getProducts(request):
	products = Products.objects.all()
	serializer = ProductSerializer(products , many=True)
	return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):

	product = Products.objects.get(_id=pk)
	serializer = ProductSerializer(product, many=False)

	return Response(serializer.data)

