from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mediastore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v/(?P<slug>[A-Za-z0-9_\-]+)$', 'video.views.detail',
        name='video_detail'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^' + settings.MEDIA_URL[1:] +
             '(?P<path>.+)$', 'video.views.debug_get_media'),
    )
