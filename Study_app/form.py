from django import forms
from Study_app.models import Crescentlib

class crescentForm(forms.ModelForm):
    class Meta:
        model=Crescentlib
        fields=['book', 'read']