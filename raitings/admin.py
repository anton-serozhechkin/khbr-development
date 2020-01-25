from django.contrib import admin
from .models import Raiting

class RaitingAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('created', 'is_active', 'author')
    search_fields = ('title', 'slug', 'overview', 'content', 'author')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        ('Основная информация', {
            'fields':(
                'title',
                'slug',
                'overview',
                'content',
                'thubmnail',
                'author'
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('is_active', 'created', 'previous_raiting', 'next_raiting')
            }
            )
    )

admin.site.register(Raiting, RaitingAdmin)
