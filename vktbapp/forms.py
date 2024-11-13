from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import usermod

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = usermod
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = usermod
        fields = ("username", "email")