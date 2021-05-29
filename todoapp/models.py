from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    for_how=models.CharField(max_length=55 ,blank=True)
    active =models.BooleanField(default=True)
    
class Repo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100,blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title