from email.headerregistry import Address
from email.policy import default
from telnetlib import STATUS
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class donermodel(models.Model):
    Name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    Address=models.CharField(max_length=200)
    credit=models.IntegerField(max_length=300)
    payment=models.CharField(max_length=5)
    def __str__(self):
        return self.Name

    
