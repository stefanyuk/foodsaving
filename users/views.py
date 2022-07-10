from django.shortcuts import redirect, render

from .forms import UserForm
from .services import UserService


def create_user(request):
    """Create new user."""
    user_srv = UserService()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = user_srv.new_user(form.cleaned_data)
            return redirect("admin/")
    else:
        form = UserForm()

    return render(request, "users/add_user.html", context={"form": form})
