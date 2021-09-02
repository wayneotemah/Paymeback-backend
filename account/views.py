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
        try:
            accounts = Account.objects.all()
            serializer = accountSerializer(accounts, many = True)
            return Response(serializer.data)
        except Account.DoesNotExist:
           return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        

    def post(self, request):
        try:
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # token=Token.objects.get(user=account).key
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

class accountDetails(APIView):
    """
    class to get(all records of a specific user), put(a single customer) and delete a single customer
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request,pk,format=None):
        try:
            user = Account.objects.get(pk=pk)
            serializer = accountSerializer(user)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def put(self,request,pk,format=None):
        #one involved in any transaction with the users
        try:
            clients = Account.objects.get(pk=pk)
            serializer = accountSerializer(clients, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)


    def delet(self, request, pk, format=None):
        try:
            client = Account.objects.get(pk=pk)
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)