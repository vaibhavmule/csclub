from django import forms

from jobboard.models import Job
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'text',)
        widgets = {
            'text': CKEditorWidget(),
        }
