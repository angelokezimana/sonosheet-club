from django.urls import re_path

from . import views  # import views so we can use them in urls.


app_name = 'store'
urlpatterns = [
    re_path(r'^$', views.listing, name='listing'),
    re_path(r'^(?P<album_id>\d+)$', views.detail, name='detail'),
    re_path(r'^search/$', views.search, name='search'),
]
