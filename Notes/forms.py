from django import forms 
from django.forms import ModelForm

from .models import Document

# create notes form
class NoteForm(ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }