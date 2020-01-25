from django.contrib import admin
from .models import *

class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', )
    list_filter = ('timestamp', )
    search_fields = ('email', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('name', )
    search_fields = ('name', 'slug')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('categories', 'created', 'is_active')
    search_fields = ('title', 'slug', 'content', 'author', 'categories')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        ('Основная информация', {
            'fields':(
                'title',
                'slug',
                'categories',
                'overview',
                'content',
                'thubmnail',
            )
        }),
        ('Дополнительные опции',
            {
            'classes': ('collapse', ),
            'fields': ('author', 'is_active',
                        'created', 'previous_post',
                        'next_post')
            }
            )
    )
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Author, AuthorAdmin)