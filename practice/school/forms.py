from django import forms
from school.models import Registration

class RegistrationForm(forms.Form):
    class Meta:
        model = Registration
        feilds = ('__All__')
