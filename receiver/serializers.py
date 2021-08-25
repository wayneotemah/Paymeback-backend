from .models import Receiver
from rest_framework import serializers

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['transactor','name','phoneNumber']