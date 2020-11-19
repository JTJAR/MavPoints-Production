from django.utils import timezone
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.conf import settings

# Create your models here.
Roles = (
    ('employee', 'EMPLOYEE'),
    ('customer', 'CUSTOMER'),
)


# class CustomUser(AbstractUser):
#     role = models.CharField(max_length=50, choices=Roles, default='employee')


class Customer(AbstractUser):
    role = models.CharField(max_length=50, choices=Roles, default='customer')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    cust_bill_card = CardNumberField('card number', null=True, blank=True)
    cust_bill_expiry = CardExpiryField('expiration date', null=True, blank=True)
    cust_bill_code = SecurityCodeField('security code', null=True, blank=True)
    total_points = models.DecimalField(max_digits=10, decimal_places=0, default = 0)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def spend_points(self, cost):
        self.total_points = self.total_points - cost
        self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.full_name)


# class RewardsAccount(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total_points = models.CharField(max_length=100, default=0)
#
#     def __str__(self):
#         return '{}'.format(self.id)

# class Employee(models.Model):
#     role = models.CharField(max_length=50, choices=Roles, default='employee')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=50)
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     updated_date = models.DateTimeField(auto_now_add=True)
