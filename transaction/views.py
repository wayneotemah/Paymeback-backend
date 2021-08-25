from django.shortcuts import render
from .models import Transaction
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class TransactionListView(APIView):
    def get(self, request):
        customer = Transaction.objects.all()
        serializer = TransactionSerializer(customer, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TransactionDetails(APIView):

    def get_object(self,transactor):
        try:
            return Transaction.objects.get(pk=transactor)
        except Transaction.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
     
    def get(self,request,transactor,format=None):
        transaction = self.get_object(transactor)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self,request,transactor,format=None):
        transaction = self.get_object(transactor)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, transactor, format=None):
        transaction = self.get_object(transactor)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

