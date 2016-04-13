from django import forms


class MailMeForm(forms.Form):
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
