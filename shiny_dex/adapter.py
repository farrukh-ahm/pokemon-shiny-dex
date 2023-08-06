from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_user_signed_up_redirect_url(self, request, user):
        return reverse('home')  # Replace 'home' with the name of your homepage URL pattern

    def get_email_confirmation_redirect_url(self, request, emailconfirmation):
        return reverse('home')  # Replace 'home' with the name of your homepage URL pattern

    def get_password_change_redirect_url(self, request, user):
        return reverse('home')  # Replace 'home' with the name of your homepage URL pattern

    def get_password_set_redirect_url(self, request, user):
        return reverse('home')  # Replace 'home' with the name of your homepage URL pattern
