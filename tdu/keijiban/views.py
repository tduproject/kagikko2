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
    form = PostingForm(initial={'subject':posts.subname})
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

    page = _get_page(
        Posting.objects.order_by('-id'),  # 投稿を新しい順に並び替えて取得する
        request.GET.get('page')  # GETクエリからページ番号を取得する
    )
    contexts = {
        'page': page,
        'posts': posts,
        'form': form,
    }
    return render(request, 'keijiban/index.html', contexts)
