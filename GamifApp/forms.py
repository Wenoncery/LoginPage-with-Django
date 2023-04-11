from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """
    Override the default user creation form by
    adding the email as a required field
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Getting the metadata from the User model
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        """
        Overriding the save method in order to create
        a user using an email address too
        """
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
