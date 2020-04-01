# file mygame/web/chargen/forms.py

from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Merit Name', max_length=80)
    category = forms.CharField(label='Merit Category',required = False)
    range = forms.CharField(label='Range',required = False)
    noteRestrictions = forms.CharField(label='Valid notes',required = False)
    prereq = forms.CharField(label='Prerequisites',
                             widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    cost = forms.CharField(label='Cost',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required = False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    recalc = forms.BooleanField(required = False)
    cg_only = forms.BooleanField(required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)