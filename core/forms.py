from django import forms
from .models import Wefunder


class WefunderForm(forms.ModelForm):
    class Meta:
        model = Wefunder
        fields = ('project_name', 'project_description','pdf_file')
