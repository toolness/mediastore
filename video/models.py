from django.db import models
from django.core.urlresolvers import reverse

class Video(models.Model):
    '''
    A video.
    '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(
        help_text="The full name of the video.",
        max_length=100
    )
    slug = models.SlugField(
        help_text="A short identifier for the video, used in "
                  "URLs and such. Only letters, numbers, underscores, and "
                  "hyphens are allowed.",
        unique=True
    )
    description = models.TextField(
        help_text="Description of the video. Can contain HTML.",
        blank=True
    )
    source = models.FileField(
        help_text="Source file for the video. Must be video/mp4."
    )
    poster_frame_with_play_button = models.ImageField(
        help_text=("Poster frame for the video with a play button "
                   "superimposed on it."),
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('video_detail', args=(self.slug,))

    def get_embed_html5(self, request):
        return '<video controls src="%s"></video>' % (
            request.build_absolute_uri(
                reverse('video_source', args=(self.slug,))
            )
        )

    def get_embed_html4(self, request):
        href = request.build_absolute_uri(
            reverse('video_detail', args=(self.slug,))
        )
        src = request.build_absolute_uri(
            reverse('video_poster_frame_with_play_button',
                    args=(self.slug,))
        )

        return '<a href="%s"><img src="%s"></a>' % (href, src)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is not None:
            # http://stackoverflow.com/a/8342249
            old_self = Video.objects.get(id=self.id)
            if old_self.source != self.source:
                old_self.source.delete(save=False)
            if (old_self.poster_frame_with_play_button and
                (old_self.poster_frame_with_play_button !=
                 self.poster_frame_with_play_button)):
                old_self.poster_frame_with_play_button.delete(
                    save=False
                )
        super(Video, self).save(*args, **kwargs)
