from django import forms


class EditForm(forms.Form):
    longname = forms.CharField(label='Clan Name', max_length=80)
    favored_attributes = forms.CharField(label='Clan Favored Attributes',required = False)
    favored_disciplines = forms.CharField(label='Clan Favored Disciplines',required = False)
    reference = forms.CharField(label='Reference', required = False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    bloodline = forms.BooleanField(required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)
