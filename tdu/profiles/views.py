from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def profile_detail(request, pk):
    post = get_object_or_404(UserProfile, pk=pk)
    #return HttpResponse(request.user.email)
    return render(request, 'profiles/profile_detail.html', {'post': post})

@login_required
def profile_mydetail(request):
    email = request.user.email
    post = UserProfile.objects.get(email = email)
    return render(request, 'profiles/profile_mydetail.html', {'post': post})

@login_required
def profile_edit(request):
    email = request.user.email
    post = UserProfile.objects.get(email = email)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile_mydetail')
    else:
        form = UserProfileForm(instance=post)
    return render(request, 'profiles/profile_edit.html', {'form': form})
