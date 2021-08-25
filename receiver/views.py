from django.shortcuts import render
from .models import Receiver
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import ReceiverSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class ReceiverListView(APIView):
    def get(self, request):
        owner = Receiver.objects.all()
        serializer = ReceiverSerializer(owner, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceiverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceiverDetails(APIView):

    def get_object(self,transactor):
        try:
            return Receiver.objects.get(pk=transactor)
        except Receiver.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
     
    def get(self,request,transactor,format=None):
        receiver = self.get_object(transactor)
        serializer = ReceiverSerializer(receiver)
        return Response(serializer.data)

    def put(self,request,transactor,format=None):
        receiver = self.get_object(transactor)
        serializer = ReceiverSerializer(receiver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delet(self, request, transactor, format=None):
        receiver = self.get_object(transactor)
        receiver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
