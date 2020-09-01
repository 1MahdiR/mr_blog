from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def index(req, tag_slug=None):

    #return HttpResponse("This is the index page.")
    
    post_list = Post.objects.order_by('-post_pubdate')
    post_list = post_list.filter(post_stat="published")[:5]

    return render(req, 'blog/index.html', { 'post_list': post_list })

def postTags(req, tag_slug=None):
    post_list = Post.objects.order_by('-post_pubdate')
    post_list = post_list.filter(post_stat="published")

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    return render(req, 'blog/tag.html', { 'post_list':post_list, 'tag':tag })

def content(req, post):
    my_post = get_object_or_404(Post, post_slug=post, post_stat="published")
    
    #return HttpResponse("This is post '%s'." % my_post.post_title)

    # List of active comments for this post!
    comments = my_post.comments_post.filter(active=True)

    new_comment = None

    if req.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=req.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = my_post
            new_comment.user = req.user
            # Save the comment to the database
            new_comment.save()
    else:
            comment_form = CommentForm()

    return render(req, 'blog/content.html', { 'my_post':my_post,
                                                'comments':comments,
                                                'new_comment':new_comment,
                                                'comment_form':comment_form })
