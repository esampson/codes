# file mygame/web/chargen/forms.py

from django import forms

class EditForm(forms.Form):
    longname = forms.CharField(label='Path Name', max_length=80)
    ruling_arcana = forms.CharField(label='Ruling Arcana')
    inferior_arcana = forms.CharField(label='Inferior Arcana')
    info = forms.CharField(label='Info',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required=False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),
                           required = False)
