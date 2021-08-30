from .models import Borrower
from rest_framework import serializers

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['lender','name','phoneNumber']