import os
from base64 import b64decode
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound, \
                        HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile

from .models import Video

def detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video/detail.html', {
        'DEBUG': settings.DEBUG,
        'video': video,
        'is_editable': request.user.is_superuser,
        'upload_poster_frame_on_load': (
            request.user.is_superuser and
            not video.poster_frame_with_play_button
        )
    })

def source(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return HttpResponseRedirect(video.source.url)

@login_required
@require_POST
def upload_poster_frame(request):
    video = get_object_or_404(Video, id=int(request.POST['id']))
    b64data = request.POST['dataURL'].split(',')[1]
    video.poster_frame_with_play_button.save(
        '%s-poster-frame-with-play-button.jpg' % video.slug,
        ContentFile(b64decode(b64data))
    )
    return HttpResponseRedirect(reverse(
        'video_detail',
        args=(video.slug,)
    ))

def debug_get_media(request, path):
    if settings.DEBUG:
        abspath = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(abspath):
            return HttpResponse(
                open(abspath, 'rb').read(),
                content_type='video/mp4'
            )
    return HttpResponseNotFound()
