from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core import validators
from .models import Menu, Item, Ingredient
import datetime



def expiration_date_check(date):
    if date <=  datetime.today():
        raise forms.ValidationError('expiration date need to be a future date')



class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        expiration_date = forms.DateField(
            required=False,
            widget=SelectDateWidget(),
            validators=[expiration_date_check]
        )
        exclude = ('created_date',)
