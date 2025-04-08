from django import forms

class AddToCartForm(forms.Form):
    barcode = forms.CharField(max_length=50)
    quantity = forms.IntegerField(min_value=1)
