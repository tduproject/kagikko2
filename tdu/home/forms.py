from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name','message','title')
        widgets = {
            'name': forms.TextInput(attrs={'size': 40}),
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'title': forms.TextInput(attrs={'size': 40})
        }
