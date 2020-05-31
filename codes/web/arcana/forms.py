from django import forms


class EditForm(forms.Form):
    longname = forms.CharField(label='Arcanum Name', max_length=80)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}), required=False)
    reference = forms.CharField(label='Reference', required = False)
    restricted = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)
