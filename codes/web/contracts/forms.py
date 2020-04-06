# file mygame/web/chargen/forms.py

from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Contract Name', max_length=80)
    group = forms.ChoiceField(choices=(('Regalia','Regalia'),('Court','Court'),('Goblin','Goblin')),label='Contract Category',required = False)
    category = forms.CharField(label='Contract Category',required = False)
    subgroup = forms.ChoiceField(choices=(('Royal','Royal'),('Common','Common'),('Goblin','Goblin')),required = False)
    reference = forms.CharField(label='Reference', required = False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)