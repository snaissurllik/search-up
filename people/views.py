from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from account.models import Profile, Tag
from django.views.generic import TemplateView
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import FilterForm
from redis import Redis


r = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class PeopleListView(LoginRequiredMixin, TemplateView):
    template_name = "people/list.html"

    def get(self, request, tag_slug=None, *args, **kwargs):
        self.__filter_profiles_get(tag_slug)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.__filter_profiles_post(request_data=request.POST)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = self.profiles
        context["form"] = FilterForm()
        return context

    def __get_profiles(self):
        if cache.get("profiles") is None:
            profiles = (
                Profile.objects.filter(is_public=True)
                .exclude(user=self.request.user)
                .select_related("user", "country", "region")
                .prefetch_related("tags")
            )
            cache.set("profiles", profiles, timeout=10)
            return profiles
        return cache.get("profiles")

    def __filter_profiles_get(self, tag_slug):
        profiles = self.__get_profiles()
        if tag_slug is None:
            self.profiles = profiles
        else:
            if not Tag.objects.filter(slug=tag_slug).exists():
                return HttpResponseBadRequest("Invalid url")
            self.profiles = profiles.filter(tags__slug__in=[tag_slug])
        return self.profiles

    def __filter_profiles_post(self, request_data):
        tags = list(request_data)[3:]
        self.profiles = self.__get_profiles()
        if tags:
            self.profiles = self.profiles.filter(tags__slug__in=tags).distinct()
        if request_data["country"]:
            self.profiles = self.profiles.filter(country=request_data["country"])
        if request_data["region"]:
            self.profiles = self.profiles.filter(region=request_data["region"])
        return self.profiles


@login_required
def people_detail_view(request, profile_pk):
    profile = Profile.objects.get(pk=profile_pk)
    if r.get(f"{profile.pk}:{request.user.pk}") is None:
        r.set(f"{profile.pk}:{request.user.pk}", 1)
        profile.views += 1
        profile.save(update_fields=["views"])
    is_liked = False
    if profile.users_like.filter(id=request.user.id).exists():
        is_liked = True
    return render(
        request, "people/detail.html", {"profile": profile, "is_liked": is_liked}
    )
