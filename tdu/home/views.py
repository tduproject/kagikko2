from django.http import HttpResponse
from django.shortcuts import render

from keijiban.models import Posting
from polls.models import Poll

# Create your views here.

def show(request):
    posts_list = Posting.objects.order_by('-created_at')[:5]
    db_poll = Poll.objects.all()
    return render(request,'home/home.html',{'posts_list': posts_list,'db_poll': db_poll})
