from django.shortcuts import redirect, render
from .forms import (
    ProfileEditForm,
    RegistrationForm,
    LoginForm,
    UserEditForm,
    PhotoEditForm,
    CountryRegisterForm,
    RegionRegisterForm,
)
from .models import Region, Country, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def registration_view(request):
    if request.method == "POST":
        user_fields = RegistrationForm.fields()
        user_data = {key: request.POST[key] for key in user_fields}
        user_form = RegistrationForm(data=user_data)

        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(
                user=user,
                country=Country.objects.get(id=request.POST["country"]),
                region=Region.objects.get(id=request.POST["region"]),
            )
            return redirect("login")
    else:
        user_form = RegistrationForm()
    country_form = CountryRegisterForm()
    region_form = RegionRegisterForm()
    return render(
        request,
        "account/registration.html",
        context={
            "main_form": user_form,
            "country_form": country_form,
            "region_form": region_form,
        },
    )


class CustomLoginView(LoginView):
    authentication_form = LoginForm


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
        )
        photo_form = PhotoEditForm(instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            photo_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        photo_form = PhotoEditForm(instance=request.user.profile)
    return render(
        request,
        "account/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "photo_form": photo_form,
        },
    )
