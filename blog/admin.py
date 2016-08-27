from django.contrib import admin

from .models import Post, Comment

admin.site.empty_value_display = '(None)'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'modified_at'
    list_display = ('title', 'created_at', 'modified_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
