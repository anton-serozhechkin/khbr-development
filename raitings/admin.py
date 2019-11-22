from django.contrib import admin
from .models import Raiting

class RaitingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('created', 'is_active')
    search_fields = ('id', 'title', 'content', 'author')
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'content',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('author', 'image', 'is_active', 'created')
            }
            )
    )
admin.site.register(Raiting, RaitingAdmin)
