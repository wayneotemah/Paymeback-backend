from django.db import models
from customer.models  import Customer

#from receiver.models import  Receiver

'''
this table keeps  records of all the people have lent money to someone else
reations with the customer table, reicever table and transaction table 
one person can have borrowers
'''
class Owner(models.Model):
    transactor  = models.OneToOneField(Customer,on_delete=models.CASCADE,default=0)
    #translation = models.ForeignKey(Transaction,on_delete=models.CASCADE,default=0)#one owner many transactions
   # receiver = models.ForeignKey(Receiver) #borrower
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()


    def __str__(self):
        return f'Receiver : {self.transactor.fullName} Lender : {self.name}'
        

