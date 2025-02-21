from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Votre nom")
    email = forms.EmailField(label="Votre email")
    message = forms.CharField(widget=forms.Textarea, label="Votre message")