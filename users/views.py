from django.shortcuts import render, redirect, reverse
from .forms import UpdateUserForm, SignInForm, CreateUserForm
from django.contrib.auth import login, authenticate
from .services import user_service
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


def index(request):
    return render(request, 'users/index.html')


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
                return redirect(reverse('users:account'))
            else:
                messages.error(request, 'Invalid email or password.')

    form = SignInForm()
    return render(request, 'log_in.html', context={'form': form})


def register_user(request):
    """Create and register a new user."""

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = user_service.new_user(form.cleaned_data)
            return redirect(reverse("users:user_login"))

    form = CreateUserForm()

    return render(request, "users/user_registration.html", context={"form": form})


@login_required
def user_account(request):
    """Show user profile page."""

    orders = user_service.get_user_orders(request.user)
    if request.method == 'POST':
        update_form = UpdateUserForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(reverse('users:account'))
    else:
        update_form = UpdateUserForm(instance=request.user)
    return render(request, 'users/account.html', {'update_form': update_form, 'orders': orders})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users:account')
