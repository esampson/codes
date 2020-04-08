# file mygame/web/chargen/forms.py

from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Devotion Name', max_length=80)
    cost = forms.CharField(label='Devotion cost')
    prereq = forms.CharField(label='Prerequisites',
                             widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required = False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)