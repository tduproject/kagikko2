from django import forms
from .models import Posting
from .models import PostingSubject

class PostingForm(forms.ModelForm):

    name = forms.CharField(label="名前", required=True)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    class Meta:
        model = Posting
        fields = ('name','message','subject')
        # widgets = {
        #     'name': forms.TextInput(attrs={'size': 40}),
        #     'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        # }

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ'


class PostingSubjectForm(forms.ModelForm):

    class Meta:
        model = PostingSubject
        fields = ('subject',)
        widgets = {
            'subject': forms.TextInput(attrs={'size': 40})
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = '教科'
