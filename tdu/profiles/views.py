from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
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

        #選択された文字が正しいか検証
        for maj in ['RB', 'RD', 'RG', 'RT', 'RU']:
            if maj == request.POST["major"]:
                post.major = request.POST["major"]

        for gra in ['1年', '2年', '3年', '4年', '院1年', '院2年', '教員']:
            if gra == request.POST["grade"]:
                post.grade = request.POST["grade"]


        #form = UserProfileForm(request.POST, instance=post)
        post.name = request.POST["name"]
        post.text = request.POST["text"]
        #post.major = request.POST["major"]
        #post.grade = request.POST["grade"] #受け取ったのがPOST　
        post.save()
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.save()
        #     return redirect('profile_mydetail')
        return redirect('profile_mydetail')
    else:
        form = UserProfileForm(instance=post)
    return render(request, 'profiles/profile_edit.html', {'form': form})