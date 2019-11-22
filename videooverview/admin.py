from django.contrib import admin
from .models import VideoDownloading

class VideoDownloadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'notes', 'created', 'is_active', )
    list_filter = ('created', 'is_active')
    search_fields = ('title', 'notes')
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'url',
                'video'
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('notes', 'is_active', 'created')
            }
            )
    )


admin.site.register(VideoDownloading, VideoDownloadingAdmin)
