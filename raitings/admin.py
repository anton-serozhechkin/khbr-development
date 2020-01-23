from django.contrib import admin
from .models import Raiting

"""class RaitingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('created', 'is_active')
    search_fields = ('title', 'slug', 'content', 'author')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'slug',
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
"""
admin.site.register(Raiting)#, RaitingAdmin)
