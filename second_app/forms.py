from django import forms
from django.core import validators
from second_app.models import User


def check_for_z(value):

    if value[1].lower() != 'z':
        raise forms.ValidationError("name needs to start with z")


class FormNameForm(forms.ModelForm):

        class Meta:
            model = User
            fields = '__all__'
