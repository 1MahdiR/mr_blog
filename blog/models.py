from django.db import models
from django.utils import timezone

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
    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete = models.CASCADE,
                            related_name = 'comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
