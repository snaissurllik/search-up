from django.db import models
from django.conf import settings
from django.urls import reverse


class BaseProfileFilter(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Country(BaseProfileFilter):
    class Meta:
        verbose_name_plural = "countries"


class Region(BaseProfileFilter):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="regions", null=True
    )

    class Meta:
        verbose_name_plural = "regions"


class Tag(BaseProfileFilter):
    def get_absolute_url(self):
        kwargs = {"tag_slug": self.slug}
        return reverse("people_tag_list", kwargs=kwargs)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    tags = models.ManyToManyField(Tag, related_name="profiles")
    description = models.TextField()
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    likes = models.PositiveBigIntegerField(default=0)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="profiles_liked"
    )
    views = models.PositiveBigIntegerField(default=0)
    country = models.ForeignKey(
        Country, related_name="profiles", on_delete=models.SET_NULL, null=True
    )
    region = models.ForeignKey(
        Region, related_name="profiles", on_delete=models.SET_NULL, null=True
    )
    time_created = models.DateField(auto_now_add=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"Profile of user {self.user.username}"

    def get_absolute_url(self):
        kwargs = {"profile_pk": self.pk}
        return reverse("people_detail", kwargs=kwargs)
