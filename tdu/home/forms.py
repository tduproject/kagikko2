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

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトル'
