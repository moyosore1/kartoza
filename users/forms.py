from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Account = get_user_model()


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "home_address",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter email"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter first name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter last name"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter phone number"}
        )
        self.fields["home_address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter home address"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "confirm password"}
        )


    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "home_address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter First Name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter Last Name"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter Phone Number"}
        )
        self.fields["home_address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter Home Address"}
        )
