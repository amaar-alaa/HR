from django.db import models
from django.contrib.auth.models import User
from django.conf import settings






# Create your models here.


class Depart(models.Model):

    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=88)
    cost = models.DecimalField(max_digits=15,decimal_places=1)
    selling = models.DecimalField(max_digits=15,decimal_places=1)
    curency = models.CharField(max_length=50,choices=(("iq", "IQ"),("$", "$")),default='IQ')
    image = models.ImageField(default='default.jpg')
    desc = models.CharField(max_length=200,blank=True,null=True)
    depart = models.ForeignKey(Depart, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

        
class Curn(models.Model):
    value=models.DecimalField(max_digits=10,decimal_places=2)

    
