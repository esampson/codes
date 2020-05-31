from django import forms

class EditForm(forms.Form):
    longname = forms.CharField(label='Advantage Name', max_length=80)
    category = forms.CharField(label='Advantage Category',required = False)
    reference = forms.CharField(label='Reference', required = False)
    info = forms.CharField(label='Info',
                           widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}),required = False)
    pool = forms.BooleanField(required = False)
    energy = forms.BooleanField(required = False)
    link = forms.CharField(label='link',widget=forms.HiddenInput(),required = False)
