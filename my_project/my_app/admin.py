from django.contrib import admin
from .models import Electricity_Bill
# Register your models here.
class Electricity_BillAdmin(admin.ModelAdmin):
        list_display = ('Customer_ID','Customer_name','Bill_no','Bill_amount','Bill_date')    
    
admin.site.register(Electricity_Bill,Electricity_BillAdmin)