from django.urls import path

from .views import edit_profile_page, my_profile_page, register_request

urlpatterns = [
    path("profile/", my_profile_page, name="my_profile_page"),
    path("profile/edit/", edit_profile_page, name="edit_profile_page"),
    path("register/", register_request, name="register"),
]
