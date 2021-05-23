from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
# Create your models here.

class UserExtension(models.Model):
    SEX = (
        ('男', '男'),
        ('女', '女'),
        ('未知','未知')
    )
    pat=(
        ('猫','猫'),
        ('狗','狗'),
        ('猫和狗','猫和狗')

    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension',null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    birthday = models.DateField(null=True, blank=True,)
    image = models.ImageField( default=u"media/default.png", max_length=1000)
    gender = models.CharField(max_length=10, choices=SEX,default='未知')
    address = models.CharField(max_length=500, blank=True,null=True)
    aboutme = models.TextField(blank=True, default='该用户还没输入个人简介',null=True)
    like=models.CharField(max_length=10,choices=pat,null=True,blank=True)

    def __str__(self):
        return str(self.user)




class Dog(models.Model):
    tx=(
        ('big','大型犬'),
        ('medium','中型犬'),
        ('small','小型犬')
    )
    mc=(
        ('null','无毛犬'),
        ('short','短毛犬'),
        ('long','长毛犬')
    )

    name=models.CharField(max_length=50)
    shape=models.CharField(max_length=20,choices=tx)
    hair=models.CharField(max_length=20,choices=mc)
    image=models.URLField(max_length=1000)
    life=models.CharField(max_length=20,blank=True)
    home=models.CharField(max_length=100,blank=True)
    breed=models.CharField(max_length=500,blank=True)
    character=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return str(self.name)

class Cat(models.Model):
    tx=(
        ('大型','大型猫'),
        ('中型','中型猫'),
        ('小型','小型猫')
    )
    mc=(
        ('无毛','无毛猫'),
        ('短毛','短毛猫'),
        ('长毛','长毛猫')
    )

    name=models.CharField(max_length=50)
    shape=models.CharField(max_length=20,choices=tx)
    hair=models.CharField(max_length=20,choices=mc)
    image=models.URLField(max_length=1000)
    life=models.CharField(max_length=20,blank=True)
    home=models.CharField(max_length=100,blank=True)
    breed=models.CharField(max_length=500,blank=True)
    character=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return str(self.name)