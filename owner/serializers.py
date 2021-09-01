from .models import Owner
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['transactor','name','phoneNumber']