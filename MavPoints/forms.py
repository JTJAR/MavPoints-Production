from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'full_name',
                  'address', 'city', 'state', 'zipcode', 'phone_number',
                  'cust_bill_card', 'cust_bill_expiry', 'cust_bill_code',)


class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('email', 'full_name',
                  'address', 'city', 'state', 'zipcode', 'phone_number',
                  'cust_bill_card', 'cust_bill_expiry', 'cust_bill_code',)
