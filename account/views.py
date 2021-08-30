from django.shortcuts import render
from .models import Account
from rest_framework import status
from .serializers import accountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated


class accountListView(APIView): 
    """
    class to get all customers and post a customer records stored 
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None):
        accounts = Account.objects.all()
        serializer = accountSerializer(accounts, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = accountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            # token=Token.objects.get(user=account).key
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class accountDetails(APIView):
    """
    class to get(all records of a specific user), put(a single customer) and delete a single customer
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get_object(self,pk):
        """
        method to get objects from cutomer table
        """
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    


    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = accountSerializer(user)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        #one involved in any transaction with the users
        clients = self.get_object(pk)
        serializer = accountSerializer(clients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)