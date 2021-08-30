from .models import Account
from rest_framework import serializers

class accountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['email','username','phoneNumber','profilePic']