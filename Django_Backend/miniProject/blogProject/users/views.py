from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm
# from .models import Profile, Follow
# from django.contrib.auth.models import User

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             Profile.objects.create(user=user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'users/profile.html', {'profile_user': user})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile', username=request.user.username)
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'users/edit_profile.html', {'form': form})

# @login_required
# def follow_user(request, username):
#     user_to_follow = get_object_or_404(User, username=username)
#     Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
#     return redirect('profile', username=username)

# @login_required
# def unfollow_user(request, username):
#     user_to_unfollow = get_object_or_404(User, username=username)
#     Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
#     return redirect('profile', username=username)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileForm
from .models import Profile, Follow

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/users/templates/registration.html',
     {'form': form})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/users/templates/profile.html',
     {'profile_user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, '/home/asifjahish/vscode/web development/Django_Backend/miniProject/blogProject/users/templates/edit_profile.html', {'form': form})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', username=username)