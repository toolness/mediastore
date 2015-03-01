from django.contrib import admin

from . import models

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.Video, VideoAdmin)

admin.site.site_header = 'Toolness Media'
