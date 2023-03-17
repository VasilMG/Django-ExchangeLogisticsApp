import datetime

from django import forms

from ExchangeLogistics.exchange.models import Offer


class DatePicker(forms.DateInput):
    input_type = 'date'


class CreateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['loading_date', 'loading_country', 'loading_place',
                  'unloading_date', 'unloading_country', 'unloading_place',
                  'load_size', 'weight', 'offer_type', 'comment']
        exclude = ['created_on', 'company']
        widgets = {
            'loading_date': DatePicker,
            'unloading_date': DatePicker,
            'comment': forms.TextInput,
        }

    def clean_loading_date(self):
        entered_date = self.cleaned_data.get('loading_date')
        if entered_date < datetime.date.today():
            raise forms.ValidationError('Date cannot be in the past.')
        return entered_date

    def clean_unloading_date(self):
        entered_date = self.cleaned_data.get('unloading_date')
        loading_date = self.cleaned_data.get('loading_date')
        if entered_date < datetime.date.today():
            raise forms.ValidationError('Date cannot be in the past.')
        elif loading_date is not None and entered_date < loading_date:
            raise forms.ValidationError('The unloading date cannot be before the loading date')
        return entered_date

    def clean_weight(self):
        value = self.cleaned_data.get('weight')
        if 0 > value or value > 28:
            raise forms.ValidationError('Value must be between 0 and 28 tons')
        return value

    def clean_load_size(self):
        value = self.cleaned_data.get('load_size')
        if 0 > value or value > 15:
            raise forms.ValidationError('Value must be between 0 and 15 meters')
        return value
    
    def clean_loading_place(self):
        value = self.cleaned_data.get('loading_place')
        if not value.isalpha():
            raise forms.ValidationError("Loading place cannot contain digits.")
        return value

    def clean_unloading_place(self):
        value = self.cleaned_data.get('unloading_place')
        if not value.isalpha():
            raise forms.ValidationError("Unloading place cannot contain digits.")
        return value

    def clean_loading_country(self):
        value = self.cleaned_data.get('loading_country')
        if not value.isalpha():
            raise forms.ValidationError('Loading country cannot contain digits.')
        return value

    def clean_unloading_country(self):
        value = self.cleaned_data.get('unloading_country')
        if not value.isalpha():
            raise forms.ValidationError('Unloading country cannot contain digits.')
        return value
