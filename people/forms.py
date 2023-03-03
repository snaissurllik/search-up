from re import template
from django import forms
from account.models import Tag, Country, Region


class MultipleTagForm(forms.Form):
    template_name = "people/tag_form.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tags = Tag.objects.all()
        for tag in tags:
            self.fields[tag.slug] = forms.BooleanField(
                required=False,
                widget=forms.CheckboxInput(attrs={"style": "display: inline-block;"}),
            )


class CountryFilterForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label="Country",
        label="",
        required=False,
    )


class RegionFilterForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.none(), empty_label="Region", label="", required=False
    )


class GeoForm(CountryFilterForm, RegionFilterForm):
    template_name = "people/geo_form.html"
    field_order = (
        "country",
        "region",
    )
