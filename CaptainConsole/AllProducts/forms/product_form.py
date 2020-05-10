from django.forms import ModelForm, widgets
from AllProducts.models import Product
from django import forms


class ProductCreateForm(ModelForm):

    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'}),
            'recommended': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }