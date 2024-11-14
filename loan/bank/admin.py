from django.contrib import admin
from .models import BankLoan
class BankLoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id','loan_type','loan_amt','cust_acno','cust_name')
# Register your models here.
admin.site.register(BankLoan,BankLoanAdmin)