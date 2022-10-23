from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .decorators import guest
from .forms import AccountForm, UserForm



@login_required
def my_profile_page(request):
    return render(request, "users/myprofile.html")


@login_required
def edit_profile_page(request):
    user = request.user
    form = AccountForm(instance=user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("my_profile_page")

    context = {"form": form}
    return render(request, "users/edit_profile.html", context)


@guest
def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(
            request, "Unsuccessful registration. Invalid information."
        )
    form = UserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )
