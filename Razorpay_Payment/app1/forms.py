from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(max_length=200, required=True)
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            userprofile = UserProfile(user=user, address=self.cleaned_data['address'])
            userprofile.save()

        return user

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].initial = self.instance.address