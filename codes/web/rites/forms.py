
from django import forms

class editForm(forms.Form):
    longname = forms.CharField(label='Werewolf rite name', max_length=80)
    type = forms.ChoiceField(choices=(('Wolf','Wolf'), ('Pack','Pack')),
                              label='Rite Category', required=False)
    rank = forms.CharField(label='Werewolf rite rank')
    prereq = forms.CharField(label='Prerequisites',
                             widget=forms.Textarea(
                                 attrs={'rows': 4, 'cols': 80}), required=False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(
                               attrs={'rows': 4, 'cols': 80}),required = False)
    reference = forms.CharField(label='Reference', required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',
                           widget=forms.HiddenInput(),required = False)