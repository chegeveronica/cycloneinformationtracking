from django.db import models

# Create your models here.

class Cyclone_info(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length = 200, default='')
    title = models.CharField(max_length=200)    
    image = models.CharField(max_length=200, default='', unique=True)    
    #link = models.CharField(max_length=2083, default='', unique=True)    
    #published = models.DateTimeField()    
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    
    source = models.CharField(max_length=30, default='', blank=True, null=True)
    
    

