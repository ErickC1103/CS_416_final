from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import WishlistItem

class TicketForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['tickets']
        widgets = {
            'tickets': forms.NumberInput(attrs={'class': 'form-control', 'min': 1})
        }

        class LoginForm(AuthenticationForm):
            username = forms.CharField(
                widget=forms.TextInput(attrs={
                    "class": "form-control text-primary",
                    "placeholder": "Username",
                })
            )
            password = forms.CharField(
                widget=forms.PasswordInput(attrs={
                    "class": "form-control",
                    "placeholder": "Password"
                })
            )
