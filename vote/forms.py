# elections/forms.py
from django import forms
from .models import Voter, ElectionOfficer
from django.contrib.auth.hashers import make_password

class VoterRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Voter
        fields = ['id_number', 'profile_picture', 'fullname', 'username', 'phone_number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        cleaned_data['password'] = make_password(password)
        return cleaned_data


class ElectionOfficerRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ElectionOfficer
        fields = ['id_number', 'profile_picture', 'fullname', 'username', 'phone_number', 'email', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        cleaned_data['password'] = make_password(password)
        return cleaned_data
