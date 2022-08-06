from django import forms
from .models import ActividadContacto


class ActividadContactoForm(forms.ModelForm):
    class Meta:
        model=ActividadContacto
        fields=['usuario','mensaje']

