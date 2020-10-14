from django import forms
class FormName(forms.Form):
    FirstName=forms.CharField()
    LastName=forms.CharField()
    Email=forms.EmailField()
