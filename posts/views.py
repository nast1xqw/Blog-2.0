from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from posts.forms import PostForm
from posts.models import Post


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=request.user
            )
            return redirect('posts')  
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

def read_post():
    ...

def update_post():
    ...

def delete_post():
    ...

def list_posts():
    ...
