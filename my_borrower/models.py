from account.models import Account
from django.db import models

# Create your models here.
'''
this table contains all the records of those that have reveived a loan from someone elses. 
one person can have many lenders,
one borrower many transactions 
'''
class Borrower(models.Model):
    lender = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()


    def __str__(self):
        return f'Receiver : {self.name} |  LENDER : {self.lender.username}'