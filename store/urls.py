from django.urls import re_path

from . import views  # import views so we can use them in urls.


urlpatterns = [
    re_path(r'^$', views.listing),
    re_path(r'^(?P<album_id>\d+)$', views.detail),
    re_path(r'^search/$', views.search),
]
