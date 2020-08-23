from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("post_title", "post_slug", "post_pubdate", "post_stat")
    list_filter = ("post_pubdate",)
    search_fields = ["post_body", "post_title"]

admin.site.register(Post, PostAdmin)
