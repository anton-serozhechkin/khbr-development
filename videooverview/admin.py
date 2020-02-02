from django.contrib import admin
from .models import Video

class VideoDownloadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'is_active', )
    list_filter = ('created', 'is_active')
    search_fields = ('title', 'notes')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        ('Основная информация', {
            'fields':(
                'title',
                'slug',
                'overview',
                'url',
                'video',
                'content',
                'author'
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('is_active', 'created', 'previous_video', 'next_video')
            }
            )
    )


admin.site.register(Video, VideoDownloadingAdmin)
