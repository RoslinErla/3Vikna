from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets
from cart.models import Checkout
from django import forms

city_choices = [('1', 'Reykjavík'), ('2', 'Seltjarnarnes'), ('3', 'Vogar'), ('4', 'Kópavogur'), ('5', 'Garðabær'),
                ('6', 'Hafnarfjörður'), ('7', 'Álftanes'), ('8', 'Reykjanesbær'), ('9', 'Grindavík'), ('10', 'Sandgerði'),
                ('11', 'Garður'), ('12', 'Mosfellsbær'), ('13', 'Akranes'), ('14', 'Borgarnes'), ('15', 'Reykholt'),
                ('16', 'Stykkishólmur'), ('17', 'Grundarfjörður'), ('18', 'Ólafsvík'), ('19', 'Snæfellsbær'),
                ('20', 'Hellissandur'), ('21', 'Búðardalur'), ('22', 'Reykhólahreppur'), ('23', 'Ísafjörður'),
                ('24', 'Bolungarvík'), ('25', 'Súðavík'), ('26', 'Patreksfjörður'), ('27', 'Tálknafjörður'),
                ('28', 'Hólmavík'), ('29', 'Drangsnes'), ('30', 'Hvammstangi'), ('31', 'Blönduós'), ('32', 'Skagaströnd'),
                ('33', 'Sauðárkrókur'), ('34', 'Varmahlíð'), ('35', 'Hofsós'), ('36', 'Siglufjörður'), ('37', 'Akureyri'),
                ('38', 'Grenivík'), ('39', 'Grímsey'), ('40', 'Dalvík'), ('41', 'Ólafsfjörður'), ('42', 'Hrísey'),
                ('43', 'Húsavík'), ('44', 'Fosshóll'), ('45', 'Laugar'), ('46', 'Mývatn'), ('47', 'Kópasker'),
                ('48', 'Raufarhöfn'), ('49', 'Þórshöfn'), ('50', 'Bakkafjörður'), ('51', 'Vopnafjörður'),
                ('52', 'Egilsstaðir'), ('53', 'Seyðisfjörður'), ('54', 'Borgarfjörður eystri'), ('55', 'Reyðarfjörður'),
                ('56', 'Eskifjörður'), ('57', 'Neskaupstaður'), ('58', 'Fáskrúðsfjörður'), ('59', 'Breiðdalsvík'),
                ('60', 'Djúpivogur'), ('61', 'Höfn'), ('62', 'Selfoss'), ('63', 'Hveragerði'), ('64', 'Þorlákshöfn'),
                ('65', 'Hella'), ('66', 'Hvolsvöllur'), ('67', 'Vík'), ('68', 'Kirkjubæjarklaustur'), ('69', 'Vestmannaeyjar')]


class CheckoutForm(ModelForm):

    def clean_Name_of_cardholder(self):
        Name_of_cardholder = self.cleaned_data['Name_of_cardholder']

        for letter in Name_of_cardholder:
            if letter.isdigit():
                raise ValidationError("The name can't contain a number")

        return Name_of_cardholder

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

        return CVC

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

