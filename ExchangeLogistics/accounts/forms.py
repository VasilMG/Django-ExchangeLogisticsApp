import re
from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import forms as auth_forms, get_user_model

from ExchangeLogistics.accounts.models import CompanyProfile

UserModel = get_user_model()


class CreateCompanyAccountForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        # self.the_user = kwargs.pop('user')
        # print(self.the_user)
        super(CreateCompanyAccountForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserModel
        fields = [UserModel.USERNAME_FIELD, 'password1', "password2", ]
        # fields = '__all__'
        field_classes = {"username": UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company_user = True
        user.save()
        the_profile = CompanyProfile.objects.create(
            user=user,
        )
        if commit:
            the_profile.save()
        return user


class CreateCompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ['user']

    def clean_phone_number(self):
        value = self.cleaned_data.get('phone_number')
        pattern = r'(\+\d{9,15}$)'
        the_match = re.match(pattern, value)
        if not the_match:
            raise forms.ValidationError("Value must start with '+' followed by 9 up to 15 digits.")
        return value

    def clean_city(self):
        value = self.cleaned_data.get('city')
        if not value.isalpha():
            raise forms.ValidationError("City cannot contain digits.")
        return value

    def clean_country(self):
        value = self.cleaned_data.get('country')
        if not value.isalpha():
            raise forms.ValidationError('Country cannot contain digits.')
        return value

    def clean_contact_person(self):
        value = self.cleaned_data.get('contact_person')
        if any(char.isdigit() for char in value):
            raise forms.ValidationError('The name cannot contain digits.')
        return value
