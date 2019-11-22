from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active',)
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ('is_active', )
    list_filter = ('name', 'is_active')
    search_fields = ('name', 'slug')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'category', 'created', 'is_active',)
    list_editable = ('is_active', )
    list_filter = ('category', 'created', 'is_active')
    search_fields = ('id', 'title', 'content', 'author',  'category')
    fieldsets = (
        (None, {
            'fields':(
                'title',
                'category',
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)