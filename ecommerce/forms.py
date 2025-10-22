from django import forms
from django.forms import ModelForm
from .models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email', 'message']


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )



