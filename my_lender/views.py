from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Lender
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import lenderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated



class lenderListView(APIView):
    """
    class to get all transactions and post a transaction records stored 
    """
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        lender = Lender.objects.all()
        serializer = lenderSerializer(lender,many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = lenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class lenderDetails(APIView):
    """
    class to get(all records of a specific user), put(a single owner) and delete a single owner
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

   
    def get_object(self,pk):
        """
        method to get objects from owner table
        """
        try:
            return Lender.objects.get(transactor=pk)
        except Lender.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
     
    def get(self,request,pk,format=None):
        lender = Lender.objects.filter(transactor=pk)
        serializer = lenderSerializer(lender, many = True)
        return Response(serializer.data)#TO DO: SHOW 404 ERROR WHEN OWNER IS NOT FOUND
        

    def put(self,request,pk,format=None):
        lender = self.get_object(pk)
        serializer = lenderSerializer(lender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, pk, format=None):
        lender = self.get_object(pk)
        lender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
