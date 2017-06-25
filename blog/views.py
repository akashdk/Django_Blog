from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
import datetime
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect



def post_list(request):
	posts = Post.published.all()
	return render(request,'blog/post/list.html', {'posts':posts})
	
def post_detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day )
	return render(request,
				  'blog/post/detail.html',
				  {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

