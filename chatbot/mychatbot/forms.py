from django import forms
from django.forms import TextInput, EmailInput

class ContactForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name', 'style': 'width: 200px;', 'class': 'form-control'}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'style': 'width: 200px;', 'class': 'form-control'}))
        category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
        subject = forms.CharField(required=False)
        body = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))