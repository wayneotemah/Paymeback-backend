from .models import Lender
from rest_framework import serializers

class lenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ['receiver','name','phoneNumber']