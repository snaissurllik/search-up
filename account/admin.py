from django.contrib import admin
from .models import Profile, Tag, Country, Region


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tags_",
        "photo",
        "country",
        "region",
        "likes",
        "views",
        "is_public",
    )
    list_filter = ("likes", "views")
    search_fields = ("user",)

    @admin.display(empty_value="Unknown")
    def tags_(self, obj):
        return list(obj.tags.all())


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "regions_")
    prepopulated_fields = {"slug": ("title",)}

    @admin.display(empty_value="No regions")
    def regions_(self, obj):
        return list(obj.regions.all())


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "country")
    prepopulated_fields = {"slug": ("title",)}
