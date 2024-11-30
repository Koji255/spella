from django import forms

class TextInputForm(forms.Form):
    '''Form for user's input text'''
    text = forms.CharField(widget=forms.Textarea, label=False, max_length=10000)