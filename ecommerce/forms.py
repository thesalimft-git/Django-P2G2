from django import forms


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
    
