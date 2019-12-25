"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin
# from django.urls import path, include

# from bookmark.views import BookmarkLV, BookmarkDV
from mysite.view import HomeView

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  url(r'admin/', admin.site.urls),
                  # Admin 사이트에 대한 URLconf인 admin.site.urls를 재활용할 때는
                  # 예외적으로 include()를 사용하지 않아도 가능하다.
                  # url(r'^admin/', admin.site.urls),
                  # url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
                  url(r'bookmark/', include('bookmark.urls', namespace='bookmark')),
                  url(r'blog/', include('blog.urls', namespace='blog')),

                  ##
                  url(r'^$', HomeView.as_view(), name='home'),

                  # Class-based views for Bookmark app
                  # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
                  # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

                  #
                  url(r'^blog/', include('blog.urls'), name='blog'),
                  # photo
                  url(r'^photo/', include('photo.urls'), name='photo'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
