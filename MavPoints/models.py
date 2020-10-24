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
    cust_bill_card = CardNumberField('card number', null=True)
    cust_bill_expiry = CardExpiryField('expiration date', null=True)
    cust_bill_code = SecurityCodeField('security code', null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.full_name)


class Employee(models.Model):
    role = models.CharField(max_length=50, choices=Roles, default='employee')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
