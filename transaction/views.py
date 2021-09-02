from django.shortcuts import render
from .models import Transaction
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated



class TransactionListView(APIView):
    """
    class to get all transactions and post a transaction records stored 
    """
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
    """
    class to get(all records of a specifi user), put(a single transaction) and delete a single transaction
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

     
    def get(self,request,pk,format=None):
        transaction = Transaction.objects.filter(pk=pk)
        serializer = TransactionSerializer(transaction, many = True)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        try:
            transaction =  Transaction.objects.get(pk=pk)

            serializer = TransactionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Transaction.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)



    def delet(self, request, pk, format=None):
        try:
            transaction =  Transaction.objects.get(pk=pk)
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Transaction.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
