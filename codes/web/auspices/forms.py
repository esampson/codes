# file mygame/web/chargen/forms.py

from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Auspice Name', max_length=80)
    auspice_skills = forms.CharField(label='Auspice Skills')
    renown = forms.CharField(label='Renown')
    auspice_gifts = forms.CharField(label='Auspice Skills')
    info = forms.CharField(label='Info',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required=False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),
                           required = False)