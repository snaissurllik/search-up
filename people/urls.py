from django.urls import path
from . import views


urlpatterns = [
    path("", views.PeopleListView.as_view(), name="people_list"),
    path(
        "<slug:tag_slug>/",
        views.PeopleListView.as_view(),
        name="people_tag_list",
    ),
    path("detail/<int:profile_pk>/", views.people_detail_view, name="people_detail"),
]
