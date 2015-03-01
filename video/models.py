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

    def get_absolute_url(self):
        return reverse('video_detail', args=(self.slug,))

    def __unicode__(self):
        return self.name
