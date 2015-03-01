import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound

from .models import Video

def detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video/detail.html', {
        'DEBUG': settings.DEBUG,
        'video': video
    })

def debug_get_media(request, path):
    if settings.DEBUG:
        abspath = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(abspath):
            return HttpResponse(
                open(abspath, 'rb').read(),
                content_type='video/mp4'
            )
    return HttpResponseNotFound()
