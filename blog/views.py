from django.shortcuts import render, get_list_or_404
from .models import Posts

# Create your views here.
def render_posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def detalles_post(request, post_id):
    post = get_list_or_404(Posts, pk=post_id)
    return render(request, 'detalles_post.html', {"post":post})