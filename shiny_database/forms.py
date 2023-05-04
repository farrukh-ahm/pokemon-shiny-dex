from django import forms
from django.utils.translation import gettext_lazy as _


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_("First name"))
    last_name = forms.CharField(max_length=30, label=_("Last name"))
    username = forms.CharField(max_length=30, label=_("User name"), help_text=_("Will be shown e.g. when commenting."))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.save()
