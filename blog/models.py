from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 100)
    post_slug = models.SlugField(max_length = 100)
    post_body = models.TextField()
    post_pubdate = models.DateTimeField(default = timezone.now)
    post_stat = models.CharField(choices = (
                                            ('draft', 'Draft'),
                                            ('published', 'Published'),
                                            ), default = 'published', max_length=10)
    
    tags = TaggableManager()

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete = models.CASCADE,
                            related_name = 'comments_post')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments_user')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'
