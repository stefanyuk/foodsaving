
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import password_validation
from .models import User


class UpdateUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class CreateUserForm(UserCreationForm):
    """Class to represent fields that should be in the user creation form."""
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Password"
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Confirm password"
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification."
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password1",
            "password2",
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email Address"}
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', "placeholder": "First Name"}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', "placeholder": "Last Name"}
            ),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', "placeholder": "Phone Number"}
            )
        }


class SignInForm(forms.Form):
    """Class to represent fields that should be in the authentication form."""

    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
