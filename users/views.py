from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AccountForm


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
    
    context = {'form':form}
    return render(request, "users/edit_profile.html", context)
