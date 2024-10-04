from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Post, Comment
# from .forms import PostForm, CommentForm

# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comment_set.all().order_by('-created_at')
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         comment_form = CommentForm()
#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# @login_required
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_form.html', {'form': form})

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user != post.author:
#         return redirect('post_detail', pk=post.pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_form.html', {'form': form})

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user != post.author:
#         return redirect('post_detail', pk=post.pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_confirm_delete.html', {'post': post})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_list.html',
     {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all().order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_list.html',
     {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_form.html',
     {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_form.html',
     {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_form.html', {'post': post})



    # /home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/blog/templates/post_form.html


    # blog/post_confirm_delete.html