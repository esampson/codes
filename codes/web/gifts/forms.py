
from django import forms

class EditForm(forms.Form):
    longname = forms.CharField(label='Gift Name', max_length=80)
    category = forms.ChoiceField(choices=(
        ('Moon','Moon'),('Shadow','Shadow'),('Wolf','Wolf')),
        label='Gift Category')
    group = forms.CharField(label='Gift Group')
    rank = forms.CharField(label='Gift Rank', required=False)
    renown = forms.ChoiceField(choices=(
        ('Cunning','Cunning'),('Glory','Glory'),('Honor','Honor'),
        ('Purity','Purity'),('Wisdom','Wisdom')))
    info = forms.CharField(
        label='Info',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}), required=False)
    reference = forms.CharField(label='Reference', required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),
                           required = False)
