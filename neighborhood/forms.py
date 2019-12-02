from django import forms
from .models import Profile,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']

class ProstForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']

