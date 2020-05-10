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
            'manufacturer': widgets.Select(attrs={'class': 'form-control'}, choices=(("Nintendo", "Nintendo"),
                                                                                     ("Sega", "Sega"),
                                                                                     ("Atari", "Atari"),
                                                                                     ("Playstation", "Playstation"))),
            'type': widgets.Select(attrs={'class': 'form-control'}, choices=(("Games", "Games"),
                                                                             ("Consoles", "Consoles"),
                                                                             ("Merchandise", "Merchandise"),
                                                                             ("Accessories", "Accessories"))),
            'recommended': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
