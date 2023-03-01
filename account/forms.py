from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Region, Country, Profile, Tag


class CountryRegisterForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label="Country",
        label="",
        required=True,
    )


class RegionRegisterForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.none(), empty_label="Region", label="", required=True
    )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        min_length=5,
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
        label="",
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Email"}), label=""
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}), label=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}), label=""
    )

    field_order = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    @classmethod
    def fields(cls):
        return cls.declared_fields.keys()  # type: ignore


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={"placeholder": "Username or email"}),
        label="",
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        label="",
    )


class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True, widget=forms.TextInput(attrs={"value": "adj"})
    )
    email = forms.EmailField(disabled=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
        label="",
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
        label="",
        required=False,
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class ProfileEditForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Describe yourself!", "rows": 3}),
        label="",
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        label="",
        widget=forms.SelectMultiple,
        required=False,
    )
    is_public = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"role": "switch"}),
    )

    class Meta:
        model = Profile
        fields = ("description", "tags", "is_public")


class PhotoEditForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput, label="", required=False)

    class Meta:
        model = Profile
        fields = ("photo",)
