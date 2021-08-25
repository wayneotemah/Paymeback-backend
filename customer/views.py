from django.shortcuts import render
from .models import Customer
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class CustomerListView(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetails(APIView):

    def get_object(self,phoneNumber):
        try:
            return Customer.objects.get(pk=phoneNumber)
        except Customer.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
     
    def get(self,request,phoneNumber,format=None):
        customer = self.get_object(phoneNumber)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self,request,phoneNumber,format=None):
        customer = self.get_object(phoneNumber)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, phoneNumber, format=None):
        customer = self.get_object(phoneNumber)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

