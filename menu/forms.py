from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core import validators
from .models import Menu
import datetime



def expiration_date_check(date):
    if date <=  datetime.date.today():
        raise forms.ValidationError('expiration date need to be a future date')



class MenuForm(forms.ModelForm):
    expiration_date = forms.DateField(
        required=False,
        widget=SelectDateWidget(),
        validators=[expiration_date_check]
    )
    class Meta:
        model = Menu
        exclude = ('created_date',)
