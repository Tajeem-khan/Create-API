from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Product
from . serializer import Productserializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class productclassview(APIView):
    def get (self, request, pk=None,):
        if pk:
            product = Product.objects.get(id=pk)
            serializer = Productserializer(product)
            return Response({"status":"success","data":serializer.data},status =status.HTTP_200_OK)
        else:
            products  = Product.objects.all()
            serializer = Productserializer(products,many=True)
            return Response({"status":"success","data":serializer.data},status =status.HTTP_200_OK)
    
    
    def post (self,request,*args,**kwargs):
        serializer = Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status =status.HTTP_200_OK)
        else:
            return Response({"status":"failed","data":serializer.errors},status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self,request,pk=None):
        product = Product.objects.get(id=pk)
        serializer = Productserializer(instance=product,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status =status.HTTP_200_OK)
        else:
            return Response({"status":"failed","data":serializer.errors},status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk=None):
        product = get_object_or_404(Product,id=pk)
        product.delete()
        return Response({"status":"success","data":"item deleted"})
        