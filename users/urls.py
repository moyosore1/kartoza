from django.urls import path

from .views import my_profile_page, edit_profile_page

urlpatterns = [
    path("profile/", my_profile_page, name="my_profile_page"),
    path("profile/edit/", edit_profile_page, name="edit_profile_page"),
    
]
