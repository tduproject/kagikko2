from django import forms
from .models import Posting
from .models import PostingSubject

class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ('name','message','subject')
        widgets = {
            'name': forms.TextInput(attrs={'size': 40}),
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }


class PostingSubjectForm(forms.ModelForm):

    class Meta:
        model = PostingSubject
        fields = ('subject',)
        widgets = {
            'subject': forms.TextInput(attrs={'size': 40})
        }
