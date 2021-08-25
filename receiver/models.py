from customer.models import Customer
from django.db import models

# Create your models here.
'''
this table contains all the records of those that have reveived a loan from someone elses. 
one person can have many lenders,
one borrower many transactions 
'''
class Receiver(models.Model):
    transactor = models.OneToOneField(Customer,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()


    def __str__(self):
        return f'Receiver{self.name} |  Lender:{self.transactor.fullName}'