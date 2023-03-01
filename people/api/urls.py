from django.urls import path
from . import views


urlpatterns = [
    path("regions/", views.ListCities.as_view(), name="list_regions"),
    path("like/", views.LikeView.as_view(), name="like"),
]
