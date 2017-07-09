# ページネーター
from django.core.paginator import (
    Paginator,  # ページネーター本体のクラス
    EmptyPage,  # ページ番号が範囲外だった場合に発生する例外クラス
    PageNotAnInteger  # ページ番号が数字でなかった場合に発生する例外クラス
)
from django.shortcuts import (
    render,
    redirect,
)
from .models import Posting
from .forms import PostingForm
from .models import PostingSubject
from .forms import PostingSubjectForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from polls.models import Poll
from profiles.models import UserProfile
from django.contrib.auth.models import User

def post_list(request):
    posts = Poll.objects.all()
    return render(request, 'keijiban/post_list.html', {'posts': posts})

def _get_page(list_, page_no, count=100):
    """ページネーターを使い、表示するページ情報を取得する"""
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        # page_noが指定されていない場合、数値で無い場合、範囲外の場合は
        # 先頭のページを表示する
        page = paginator.page(1)
    return page

def index(request,pk):
    """表示・投稿を処理する"""
    posts = get_object_or_404(Poll, pk=pk)
    # 教科名と投稿名者をフォームにあらかじめ登録しておく設定
    if not request.user.is_authenticated():
        #ログインされていない場合は投稿者名が@名無しの電大生になる
        form = PostingForm(initial={'subject':posts.subname , 'name':"@名無しの電大生", 'pk_label':-1})
    else:
        #ログインされている場合は投稿者名がプロフィールの名前になる
        email = request.user.email
        info_personal = UserProfile.objects.get(email = email)
        #ユーザプロフィールへのリンク情報を付加
        link_profile = UserProfile.objects.all()
        for tmp in link_profile:
            if tmp.email == email:
                pk_link = tmp.pk

        form = PostingForm(initial={'subject':posts.subname , 'name':info_personal.name, 'pk_label':pk_link})

    if request.method == 'POST':
        # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
        form = PostingForm(request.POST or None)
        if form.is_valid():
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
            form.save()
            # メッセージフレームワークを使い、処理が成功したことをユーザーに通知する
            messages.success(request, '投稿を受付ました。')
            return redirect('keijiban:index',pk=pk)
        else:
            # メッセージフレームワークを使い、処理が失敗したことをユーザーに通知する
            messages.error(request, '入力内容に誤りがあります。')

    #リストを作成し、該当する講義のデータのみ抽出する
    db_posts = Posting.objects.order_by('-subject')
    post_list = ["temp"]
    for temp in db_posts:
        if temp.subject == posts.subname:
            post_list.append(temp)

    #リストの表示設定
    post_list.pop(0)
    post_list.reverse()

    page = _get_page(
        # Posting.objects.order_by('-id'),  # 投稿を新しい順に並び替えて取得する
        post_list,
        request.GET.get('page')  # GETクエリからページ番号を取得する
    )
    contexts = {
        'page': page,
        'posts': posts,
        'form': form,
    }
    return render(request, 'keijiban/index.html', contexts)
