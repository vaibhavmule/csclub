from django import forms

from blog.models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': CKEditorWidget(),
        }
