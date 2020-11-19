from django.contrib import admin

from .models import Customer
# from .models import Employee


class CustomerList(admin.ModelAdmin):
    list_display = ('username', 'id', 'phone_number')
    list_filter = ('username', 'id')
    search_fields = ('username',)
    ordering = ['username']


# class EmployeeList(admin.ModelAdmin):
#     list_display = ('username', 'id', 'phone_number')
#     list_filter = ('username', 'id')
#     search_fields = ('username',)
#     ordering = ['username']


admin.site.register(Customer, CustomerList)
# admin.site.register(Employee, EmployeeList)
