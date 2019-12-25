from django.conf.urls import url
from django.conf.urls.i18n import urlpatterns

from photo.views import AlbumDV, AlbumLV, PhotoDV

app_name = 'photo'
urlpatterns = [
    # Example : /
    url(r'^$', AlbumLV.as_view(), name='index'),
    # Example : /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),
    # Example /album/99/
    url(r'^album/(?P<pk>\d+)$', AlbumDV.as_view(), name='album_detail'),
    url(r'^photo/(?P<pk>\d+)$', PhotoDV.as_view(), name='photo_detail'),
]
