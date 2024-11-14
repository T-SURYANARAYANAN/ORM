# Ex02 Django ORM Web Application
## Date: 14|11|2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import BankLoan
class BankLoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id','loan_type','loan_amt','cust_acno','cust_name')
# Register your models here.
admin.site.register(BankLoan,BankLoanAdmin)

models.py

from django.db import models
from django.contrib import admin

class BankLoan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=30)
    loan_amt = models.FloatField()
    cust_acno = models.IntegerField()
    cust_name = models.CharField(max_length=50)

```



## OUTPUT

![alt text](<Screenshot 2024-11-14 143814.png>)
![alt text](<WhatsApp Image 2024-11-14 at 14.41.21_36a7ce47.jpg>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
