from django.shortcuts import render

# Create your views here.


def my_profile_page(request):
    return render(request, "users/myprofile.html")


def edit_profile_page(request):
    return render(request, "users/edit_profile.html")
