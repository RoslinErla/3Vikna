from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets
from cart.models import Checkout
from django import forms
import datetime
from datetime import datetime


city_choices = [('Reykjavík', 'Reykjavík'), ('Seltjarnarnes', 'Seltjarnarnes'), ('Vogar', 'Vogar'), ('Kópavogur', 'Kópavogur'),
                ('Garðabær', 'Garðabær'), ('Hafnarfjörður', 'Hafnarfjörður'), ('Álftanes', 'Álftanes'), ('Reykjanesbær', 'Reykjanesbær'),
                ('Grindavík', 'Grindavík'), ('Sandgerði', 'Sandgerði'), ('Garður', 'Garður'), ('Mosfellsbær', 'Mosfellsbær'),
                ('Akranes', 'Akranes'), ('Borgarnes', 'Borgarnes'), ('Reykholt', 'Reykholt'), ('Stykkishólmur', 'Stykkishólmur'),
                ('Grundarfjörður', 'Grundarfjörður'), ('Ólafsvík', 'Ólafsvík'), ('Snæfellsbær', 'Snæfellsbær'),
                ('Hellissandur', 'Hellissandur'), ('Búðardalur', 'Búðardalur'), ('Reykhólahreppur', 'Reykhólahreppur'),
                ('Ísafjörður', 'Ísafjörður'), ('Bolungarvík', 'Bolungarvík'), ('Súðavík', 'Súðavík'),
                ('Patreksfjörður', 'Patreksfjörður'), ('Tálknafjörður', 'Tálknafjörður'), ('Hólmavík', 'Hólmavík'),
                ('Drangsnes', 'Drangsnes'), ('Hvammstangi', 'Hvammstangi'), ('Blönduós', 'Blönduós'), ('Skagaströnd', 'Skagaströnd'),
                ('Sauðárkrókur', 'Sauðárkrókur'), ('Varmahlíð', 'Varmahlíð'), ('Hofsós', 'Hofsós'), ('Siglufjörður', 'Siglufjörður'),
                ('Akureyri', 'Akureyri'), ('Grenivík', 'Grenivík'), ('Grímsey', 'Grímsey'), ('Dalvík', 'Dalvík'),
                ('Ólafsfjörður', 'Ólafsfjörður'), ('Hrísey', 'Hrísey'), ('Húsavík', 'Húsavík'), ('Fosshóll', 'Fosshóll'),
                ('Laugar', 'Laugar'), ('Mývatn', 'Mývatn'), ('Kópasker', 'Kópasker'), ('Raufarhöfn', 'Raufarhöfn'),
                ('Þórshöfn', 'Þórshöfn'), ('Bakkafjörður', 'Bakkafjörður'), ('Vopnafjörður', 'Vopnafjörður'),
                ('Egilsstaðir', 'Egilsstaðir'), ('Seyðisfjörður', 'Seyðisfjörður'), ('Borgarfjörður eystri', 'Borgarfjörður eystri'),
                ('Reyðarfjörður', 'Reyðarfjörður'), ('Eskifjörður', 'Eskifjörður'), ('Neskaupstaður', 'Neskaupstaður'),
                ('Fáskrúðsfjörður', 'Fáskrúðsfjörður'), ('Breiðdalsvík', 'Breiðdalsvík'), ('Djúpivogur', 'Djúpivogur'),
                ('Höfn', 'Höfn'), ('Selfoss', 'Selfoss'), ('Hveragerði', 'Hveragerði'), ('Þorlákshöfn', 'Þorlákshöfn'),
                ('Hella', 'Hella'), ('Hvolsvöllur', 'Hvolsvöllur'), ('Vík', 'Vík'), ('Kirkjubæjarklaustur', 'Kirkjubæjarklaustur'),
                ('Vestmannaeyjar', 'Vestmannaeyjar')]


class CheckoutForm(ModelForm):

    def clean_Name_of_cardholder(self):
        Name_of_cardholder = self.cleaned_data['Name_of_cardholder']

        for letter in Name_of_cardholder:
            if letter.isdigit():
                raise ValidationError("The name can't contain a number")

        return Name_of_cardholder

    def clean_Postal_code(self):
        Postal_code = self.cleaned_data['Postal_code']

        if Postal_code < 100 or Postal_code > 902:
            raise ValidationError("Not a valid postal code")
        return Postal_code

    def clean_Full_name(self):
        Full_name = self.cleaned_data['Full_name']

        for letter in Full_name:
            if letter.isdigit():
                raise ValidationError("The name can't contain a number")

        return Full_name

    def clean_Card_number(self):
        Card_number = self.cleaned_data['Card_number']

        if len(str(Card_number)) != 16:
            raise ValidationError("This is not a valid card number")

        return Card_number

    def clean_CVC(self):
        CVC = self.cleaned_data['CVC']
        if len(str(CVC)) != 3:
            raise ValidationError("This is not a valid cvc")

        return '***'

    def clean_Expiration_date(self):
        Expiration_date = self.cleaned_data['Expiration_date']
        date = datetime.strptime(Expiration_date, '%Y-%m-%d')
        print(date)
        if date < datetime.now():
            raise ValidationError("This card has expired")

        return Expiration_date



    Full_name = forms.CharField(label='Full name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Address = forms.CharField(label='Address', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    City = forms.ChoiceField(choices=city_choices, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    Postal_code = forms.IntegerField(label='Postal code', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Name_of_cardholder = forms.CharField(label='Name of cardholder', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Card_number = forms.IntegerField(label='Card number all in one continuous string', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Expiration_date = forms.CharField(label='Expiration date (year-mm-dd)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    CVC = forms.IntegerField(label='CVC', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Checkout
        exclude = ['id']
        fields = ('Full_name', 'Address', 'City', 'Postal_code', 'Name_of_cardholder', 'Card_number', 'Expiration_date', 'CVC')

