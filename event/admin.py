from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'day', 'place', 'created', 'is_active')
    list_editable = ('day', 'place', )
    list_filter = ('place', 'day', 'created', 'author', 'is_active')
    search_fields = ('title', 'slug', 'overview', 'day', 'content', 'place')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        ('Основная информация', {
            'fields':(
                'title',
                'slug',
                'overview',
                'thubmnail',
                'day',
                'place',
                'content',
                'author',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('start_time', 'end_time',
                        'is_active', 'created',
                        'previous_event', 'next_event')
            }
            )
    )

admin.site.register(Event, EventAdmin)
