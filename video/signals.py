from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from .models import Video

@receiver(pre_delete, sender=Video)
def video_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.source.delete(False)
    if instance.poster_frame_with_play_button:
        instance.poster_frame_with_play_button.delete(False)
