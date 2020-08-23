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
        return self.post_titlie