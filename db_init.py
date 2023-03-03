import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "searchup.settings")
django.setup()

from django.utils.text import slugify
from account.models import Country, Region, Tag


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


def populate_tags():
    tags = (
        "programming",
        "web development",
        "networking",
        "cybersecurity",
        "cloud computing",
        "data science",
        "machine learning",
        "artificial intelligence",
        "big data",
        "database management",
        "software engineering",
        "operating systems",
        "virtualization",
        "containerization",
        "mobile development",
        "game development",
        "Internet of Things",
        "blockchain",
        "e-commerce",
        "digital marketing",
        "user experience",
        "user interface",
        "project management",
        "agile methodology",
        "DevOps",
    )
    for tag in tags:
        tag_slug = slugify(tag)
        Tag.objects.create(title=tag, slug=tag_slug)
        print(f'"{tag}": done...')


if __name__ == "__main__":
    print(f"{'-'*10} Populating the database with countries and regions...{'-'*10}")
    populate_geo()
    print(f"{'-'*10}Populating the database with tags...{'-'*10}")
    populate_tags()
