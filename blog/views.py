from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(req):
    #return HttpResponse("This is the index page.")
    
    post_list = Post.objects.order_by('-post_pubdate')
    post_list = post_list.filter(post_stat="published")[:5]

    return render(req, 'blog/index.html', { 'post_list': post_list })

def content(req, post):
    my_post = get_object_or_404(Post, post_slug=post, post_stat="published")
    
    #return HttpResponse("This is post '%s'." % my_post.post_title)

    return render(req, 'blog/content.html', { 'my_post':my_post })
