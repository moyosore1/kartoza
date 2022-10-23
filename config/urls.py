from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),

]
