# file mygame/web/chargen/forms.py

from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Tribe Name', max_length=80)
    renown = forms.CharField(label='Renown', required = False)
    tribe_gifts = forms.CharField(label='Tribe Gifts')
    info = forms.CharField(label='Info',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required=False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),
                           required = False)