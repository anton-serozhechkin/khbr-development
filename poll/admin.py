from django.contrib import admin
from .models import *

class PollAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'question', 'counter_votes', )
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'created', 'author__user__username', 
                    'author__user__lastname', 'question', 'content', )

class AnswerAdmin(admin.ModelAdmin):
    list_filter = ('poll__author', )
    search_fields = ('poll__title', 'poll__question', 'poll__content',
                     'poll__author', 'text', 'counter', )


class UserAnswerAdmin(admin.ModelAdmin):
    list_filter = ('poll__author', 'poll__is_active', )
    search_fields = ('poll__title', 'poll__question', 'poll__content',
                    'poll__author', 'answer__text', 'user_username',
                    'user_lastname')


admin.site.register(Poll, PollAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)