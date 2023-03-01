import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "searchup.settings")
django.setup()

from django.utils.text import slugify
from account.models import Country, Region


def populate_geo():
    with open("geo.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for country in data:
        country_name = country["countryName"]
        country_slug = slugify(country_name)
        country_created = Country.objects.create(title=country_name, slug=country_slug)
        for region in country["regions"]:
            region_name = region["name"]
            region_slug = slugify(region_name)
            Region.objects.create(
                title=region_name, slug=region_slug, country=country_created
            )
        print(f"{country_name}: done...")


if __name__ == "__main__":
    populate_geo()
