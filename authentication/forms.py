from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label 
            self.fields[fieldname].label = ''


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
