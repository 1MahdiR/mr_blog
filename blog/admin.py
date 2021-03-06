from django.contrib import admin

from .models import Post, Comment

# Register your models here.
class PostComments(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')

class PostAdmin(admin.ModelAdmin):
    list_display = ("post_title", "post_slug", "post_pubdate", "post_stat")
    list_filter = ("post_pubdate",)
    search_fields = ["post_body", "post_title"]

    inlines = [PostComments]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
