from django.db import models
from django.contrib import admin
# Create your models here.
class Electricity_Bill(models.Model):
    Customer_ID = models.CharField(max_length=50,primary_key=True)
    Customer_name = models.CharField(max_length=50)
    Bill_no = models.IntegerField()
    Bill_amount = models.IntegerField()
    Bill_date = models.DateField()
    
 
  
