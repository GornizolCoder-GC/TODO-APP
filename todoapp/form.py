from django import forms
from todoapp.models import TodoApp


class CreateForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['title', 'description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields['title'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['class'] = 'form-control'
