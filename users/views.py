from django.shortcuts import redirect, render, reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str, DjangoUnicodeDecodeError
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import CreateUserForm, SignInForm
from .services import user_service
from services.email_service import EmailService


def index(request):
    return render(request, 'users/index.html')


def register_user(request):
    """Create and register a new user."""
    email_srv = EmailService(request)

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = user_service.new_user(form.cleaned_data)
            token = default_token_generator.make_token(user)
            email_srv.send_activation_email(user, token)
            messages.success(request, 'You are signed up. To activate the account, follow the link sent to the mail.')
            return redirect(reverse("users:user_login"))

    form = CreateUserForm()

    return render(request, "users/user_registration.html", context={"form": form})


def activate_user_profile(request, uidb64, token):
    """Activate profile of the user with the provided id, if token is valid."""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user_service.get_user(user_id=uid)
    except (DjangoUnicodeDecodeError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user_service.activate_user_profile(user)
        messages.success(request, 'Thank you for your email confirmation. Now you can login to your account.')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect(reverse('users:user_login'))


def user_login(request):
    """Sign in user to the service."""
    if request.user.is_authenticated:
        return redirect(reverse('users:home'))
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect(reverse('users:home'))
            else:
                messages.error(request, 'Invalid email or password.')

    form = SignInForm()
    return render(request, 'log_in.html', context={'form': form})
