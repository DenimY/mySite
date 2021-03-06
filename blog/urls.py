from django.conf.urls import url

from blog.views import PostLV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV, PostDV, TagTV, PostTOL, SearchFormView, PostCreateView, PostChangeLV, PostUpdateView, PostDeleteView

app_name = 'blog'
urlpatterns = [
    # Example: /
    url(r'^$', PostLV.as_view(), name='index'),
    # Example: /post/ (same as /)
    url(r'^post/$', PostLV.as_view, name='post_list'),
    # Example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # Example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    # Example: /2012/nov
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    # Example: /2012/nov/10
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    #Example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    # url(r'^$', PostLV.as_view(), name='index'),

    #Example: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    #Example: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    #Example: /tag/search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    #
    url(r'^add/$', PostCreateView.as_view(), name='add'),
    url(r'^change/$', PostChangeLV.as_view(), name='change'),
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='delete'),


]
