from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserMod

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserMod
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserMod
        fields = ("username", "email")