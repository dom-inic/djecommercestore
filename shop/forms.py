from django import forms
from django.forms import ModelForm
from . models import Item

PAYMENT_CHOICES = (
    ('Mpesa', 'Mpesa'),
    ('S', 'Stripe'),
    ('P', 'PayPal'),
     
)

class NewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price', 'discount_price', 'category', 'label',  'stock_no',
        'description_short', 'description_long', 'image',
        ]
        exclude=['date_added', 'slug']
        widget = {
            'description_short' : forms.Textarea(
                attrs={
                    "required": True,
                    "placeholder": "short description for item ...",
                    "class": "form-control",
                }
            ),
            'description_long': forms.Textarea(
                attrs={
                    "required": True,
                    "placeholder": "long description for item ..",
                    "class": 'form-control',
                }
            )
        }


# class CheckoutForm(forms.Form):
#     street_address = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': '1234 Main St',
#         'class': 'form-control'
#     }))
#     apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'Apartment or suite',
#         'class': 'form-control'
#     }))
#     country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
#         'class': 'custom-select d-block w-100'

#     }))
#     zip = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     same_shipping_address = forms.BooleanField(required=False)
#     save_info = forms.BooleanField(required=False)
#     payment_option = forms.ChoiceField(
#         widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


# class CouponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code'
#     }))


# class RefundForm(forms.Form):
#     ref_code = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'rows': 4
#     }))
#     email = forms.EmailField()
