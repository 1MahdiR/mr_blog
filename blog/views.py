from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def index(req):
    #return HttpResponse("This is the index page.")
    
    post_list = Post.objects.order_by('-post_pubdate')
    post_list = post_list.filter(post_stat="published")[:5]

    return render(req, 'blog/index.html', { 'post_list': post_list })

def content(req, post):
    my_post = get_object_or_404(Post, post_slug=post, post_stat="published")
    
    #return HttpResponse("This is post '%s'." % my_post.post_title)

    # List of active comments for this post!
    comments = my_post.comments.filter(active=True)

    new_comment = None

    if req.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=req.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = my_post
            # Save the comment to the database
            new_comment.save()
    else:
            comment_form = CommentForm()

    return render(req, 'blog/content.html', { 'my_post':my_post,
                                                'comments':comments,
                                                'new_comment':new_comment,
                                                'comment_form':comment_form })

