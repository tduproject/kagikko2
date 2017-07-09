from django import forms
from .models import UserProfile


GRADE_CHOICES = (
    ('1年', '1年生'),
    ('2年', '2年生'),
    ('3年', '3年生'),
    ('4年', '4年生'),
    ('院1年', '院1年生'),
    ('院2年', '院2年生'),
    ('教員', '教員'),

)

MAJOR_CHOICES = (
    ('RB', 'RB'),
    ('RD', 'RD'),
    ('RG', 'RG'),
    ('RT', 'RT'),
    ('RU', 'RT'),
)

class UserProfileForm(forms.ModelForm):

    name = forms.CharField(label="名前", required=True)
    text = forms.CharField(label="コメント", widget=forms.Textarea)


    class Meta:
        model = UserProfile
        fields = ('name', 'grade', 'major', 'text')


    grade = forms.ChoiceField(
    label='学年',
    widget=forms.Select,
    choices=GRADE_CHOICES,
    required=False,
    )

    major = forms.ChoiceField(
    label='学系',
    widget=forms.Select,
    choices=MAJOR_CHOICES,
    required=False,
    )

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前'

        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = 'コメント'
