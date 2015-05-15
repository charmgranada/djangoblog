from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# takes a request and 
# returns a render of the template: blog/post_list.html
def post_list(request):

    # 'posts' = name of the QuerySet
    posts = Post.objects.all()
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # 'request' = everything received from the user via internet
    # {'posts':posts} = things for the template to use
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})