from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from keijiban.models import Posting
from polls.models import Poll
from .models import Contact
from .forms import ContactForm

# Create your views here.

def show(request):
    #最新スレッド5件を表示する処理
    #全てのデータを1つのlistに集約
    posts_list = Posting.objects.order_by('-created_at')
    db_poll = Poll.objects.all()
    pk_list = ["0"]
    for post in posts_list:
        for db_post in db_poll:
            if post.subject == db_post.subname:
                pk_list.append(db_post.pk)

    #科目名が同じものを取り除く
    pk_list.pop(0)
    i = 0
    n = len(pk_list)
    while i < n:
        j = 0
        while j < i:
            if pk_list[j] == pk_list[i]:
                pk_list.pop(i)
                n = n - 1
                i = 0
                break
            j = j + 1
        i = i + 1

    #5件までにまとめる
    n = len(pk_list)
    count = 5
    if n > 5:
        while count < n:
            pk_list.pop(count)
            n = n - 1

    #お問い合わせフォーム処理
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '投稿を受付ました。')
            return redirect('home:show')
        else:
            messages.error(request, '入力内容に誤りがあります。')

    contexts = {
        'posts_list': posts_list,
        'db_poll': db_poll,
        'pk_list': pk_list,
        'form':form,
    }

    return render(request,'home/home.html', contexts)
