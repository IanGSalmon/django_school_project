from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty. BAD BOT!')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Please verify your email address.')
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                                widget=forms.HiddenInput, 
                                label='Leave empty',
                                #validators=[validators.MaxLengthValidator(0)]
                                validators=[must_be_empty])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                'You need to enter the same email in both fields.')

    # Instead of using this method, we can use the above validator
    #def clean_honeypot(self):
    #    honeypot = self.cleaned_data['honeypot']
    #    if len(honeypot):
    #        raise forms.ValidationError(
    #            'honeypot should be left empty, BAD BOT!')
    #        return honeypot