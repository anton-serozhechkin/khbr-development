from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'day', 'place', )
    list_editable = ('day', 'place', )
    list_filter = ('place', 'created', 'is_active')
    search_fields = ('title', 'slug', 'notes', 'day', 'place')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'slug',
                'day',
                'place',
                'notes',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('start_time', 'end_time', 'image', 'is_active', 'created')
            }
            )
    )

admin.site.register(Event, EventAdmin)
