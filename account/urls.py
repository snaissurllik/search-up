from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.registration_view, name="register"),
    path(
        "login/",
        views.CustomLoginView.as_view(template_name="account/signin.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="account/logged_out.html"),
        name="logout",
    ),
    path("profile-edit/", views.profile_edit, name="profile"),
]
