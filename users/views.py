from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, View
from django.core.mail import send_mail
from users.forms import UserRegisterForm, UserProfileForm, UserPassRecoveryForm
from users.models import User
from config import settings
import secrets

from users.services import send_mail_for_registration


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail_for_registration(user, url)
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))



class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user