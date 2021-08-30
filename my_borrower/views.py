from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Borrower
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import BorrowerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated



class borrowerListView(APIView):
    """
    class to get all receiver and post a receiver records stored 
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        borrower = Borrower.objects.all()
        serializer = BorrowerSerializer(borrower, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BorrowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrowerDetails(APIView):
    """
    class to get(all records of a specific user), put(a single receiver) and delete a single transaction
    """
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        """
        method to get objects from receiver table
        """
        try:
            return Borrower.objects.get(transactor=pk)
        except Borrower.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
     
    def get(self,request,pk,format=None):
        borrower = Borrower.objects.filter(transactor=pk)
        serializer = BorrowerSerializer(borrower, many = True)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        borrower = self.get_object(pk)
        serializer = BorrowerSerializer(borrower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, pk, format=None):
        borrower = self.get_object(pk)
        borrower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
