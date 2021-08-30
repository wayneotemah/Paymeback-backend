from django.db import models
from django.dispatch.dispatcher import receiver
from account.models  import Account


'''
this table keeps  records of all the people have lent money to someone else
reations with the customer table, reicever table and transaction table 
one person can have borrowers
'''
class Lender(models.Model):
    receiver  = models.ForeignKey(Account,on_delete=models.CASCADE,default=0)
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()


    def __str__(self):
        return f'Receiver : {self.receiver.username} LENDER : {self.name}'
        

