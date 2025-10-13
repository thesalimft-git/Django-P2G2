from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=250,required=False)
    price = forms.DecimalField(required=False)

    
    
