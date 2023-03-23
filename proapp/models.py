from django.db import models

class portfolio(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500) 
    
# Create your models here.
