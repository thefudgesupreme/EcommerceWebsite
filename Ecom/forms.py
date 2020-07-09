from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal'),
)


class checkoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': " ABC Chowk",
        'class':"md-form mb-auto form-control"
    }))
    apartment_address = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class':"md-form mb-auto form-control"
    }))
    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    save_billing_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    billing_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
