from django.db import models
# Create your models here.
# import owner. models and reciver.models
#pushing
        
'''
table holding all the records of the people using the app. 
one one person can have many lenders, many receivers, many transactions
'''
class Customer(models.Model):
    fullName = models.CharField(max_length=250)
    phoneNumber = models.IntegerField(default=0)
    password = models.CharField(max_length=50,null= True)
    profilePic = models.ImageField(upload_to ='images/',null = True)# make a local directory to save profile pics

    def __str__(self):
        return f'{self.fullName}, {self.phoneNumber}'

    