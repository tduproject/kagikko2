# coding: UTF-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

#
# 一覧表示
#
def poll_list(request):
    posts = Poll.objects.all()
    return render(request, 'poll_list/poll_list.html', {'posts': posts})

def poll_detail(request, pk):
    post = get_object_or_404(Poll, pk=pk)
    return render(request, 'poll_list/poll_detail.html', {'post': post})

# 投票
#
def vote(request):
    name = request.POST["subname"]
    choice = Choice.objects.filter(subname = name)

    q1 = request.POST["select1"]
    q2 = request.POST["select2"]
    q3 = request.POST["select3"]

    Q1 = choice[0]
    Q2 = choice[1]
    Q3 = choice[2]

    if q1 == "e1" :
            num = Q1.easy
            Q1.easy = num+1
            Q1.save()

    elif q1 == "n1" :
            num = Q1.normal
            Q1.normal = num+1
            Q1.save()

    elif q1 == "h1" :
            num = Q1.hard
            Q1.hard = num+1
            Q1.save()

    if q2 == "e2" :
            num = Q2.easy
            Q2.easy = num+1
            Q2.save()

    elif q2 == "n2" :
            num = Q2.normal
            Q2.normal = num+1
            Q2.save()

    elif q2 == "h2" :
            num = Q2.hard
            Q2.hard = num+1
            Q2.save()

    if q3 == "e3" :
            num = Q3.easy
            Q3.easy = num+1
            Q3.save()

    elif q3 == "n3" :
            num = Q3.normal
            Q3.normal = num+1
            Q3.save()

    elif q3 == "h3" :
            num = Q3.hard
            Q3.hard = num+1
            Q3.save()

    return render(request, 'poll_list/poll_result.html', {'Q1' :Q1,'Q2': Q2,'Q3' : Q3 })
