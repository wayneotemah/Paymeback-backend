from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
        
'''
table holding all the records of the people using the app. 
one one person can have many lenders, many receivers, many transactions
'''

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,phoneNumber,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not phoneNumber:
            raise ValueError("Users Must have a phone number")
        if not username:
            raise ValueError("User muct have a username")

        user = self.model(
            email=self.normalize_email(email),
            phoneNumber = phoneNumber,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,phoneNumber,username):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phoneNumber=phoneNumber,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=50,null= True)
    phoneNumber         = models.IntegerField(unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to ='images/',null = True)# make a local directory to save profile pics

    USERNAME_FIELD = "phoneNumber"
    EMAIL_FILED = 'email'
    REQUIRED_FIELDS = ['username','email']

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.username}, {self.phoneNumber}, {self.email}'

    def has_perm(self,perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)