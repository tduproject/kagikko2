from django.shortcuts import render
from app.models import Post
from .models import Timetable1,Timetable2
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def time_table(request):
    posts = Post.objects.all()

    #return HttpResponse(request.user.email)
    return render(request, 'timetable/timetable.html', {'posts': posts})

@login_required
def time_table2(request):

    username = request.user.email
    subject = request.POST["timetable"]

    # listnames = ["月1","月2","月3","月4","月5","火]
    listnames = list()
    when = ["後期"]
    days = ["月","火","水","木","金"]
    times = ["1","2","3","4","5"]
    tuti = ["土1","土2","土3","土4"]

    #検索するリストを作成
    for day in days:
        for time in times:
            data = day + time
            listnames.append(data)
    for element in tuti:
        listnames.append(element)

    #listnamesで作られた、リストを用いて、request.Postで送信されたデータを保存
    #何も選択されていない場合、保存しない

    #現在保存されている時間割を、検索
    user_timetable1 = Timetable1.objects.filter(username = username)
    for day2 in listnames:
        week = day2[0]
        num = day2[1]
        mytime = Timetable1()
        if user_timetable1.count() == 0:
            t1 = request.POST[day2]
            if t1 == request.POST[day2]:
                if t1 != 'null':
                    mytime.username = username
                    mytime.day = day2[0]
                    mytime.time = day2[1]
                    mytime.sub = t1
                    mytime.when = "前期"
                    mytime.save()
        else:
            t1 = request.POST[day2]
            if t1 == request.POST[day2]:
                if t1 != 'null':
                    for timetable in user_timetable1:
                        if timetable.day == week  and timetable.time == num:
                            print(timetable.sub)
                            timetable.delete()
                            mytime.username = username
                            mytime.day = day2[0]
                            mytime.time = day2[1]
                            mytime.sub = t1
                            mytime.when = "前期"
                            mytime.save()
                        else:
                            mytime.username = username
                            mytime.day = day2[0]
                            mytime.time = day2[1]
                            mytime.sub = t1
                            mytime.when = "前期"
                            mytime.save()

    listnames2 = list()
    tuti2 = ["後期土1","後期土2","後期土3"]
    for day in days:
        for time in times:
            data = when[0] + day + time
            listnames2.append(data)
    for elemnt2 in tuti2:
        listnames2.append(elemnt2)


    user_timetable2 = Timetable2.objects.filter(username=username)
    for day2 in listnames2:
        week = day2[2]
        num = day2[3]
        mytime = Timetable2()
        if user_timetable2.count() == 0:
            t1 = request.POST[day2]
            if t1 == request.POST[day2]:
                if t1 != 'null':
                    mytime.username = username
                    mytime.day = day2[2]
                    mytime.time = day2[3]
                    mytime.sub = t1
                    mytime.when = "後期"
                    mytime.save()
        else:
            t1 = request.POST[day2]
            if t1 == request.POST[day2]:
                if t1 != 'null':
                    for timetable in user_timetable2:
                        if timetable.day == week and timetable.time == num:
                            timetable.delete()
                            mytime.username = username
                            mytime.day = day2[2]
                            mytime.time = day2[3]
                            mytime.sub = t1
                            mytime.when = "後期"
                            mytime.save()

                        else:
                            mytime.username = username
                            mytime.day = day2[2]
                            mytime.time = day2[3]
                            mytime.sub = t1
                            mytime.when = "後期"
                            mytime.save()
    return HttpResponseRedirect('/timetable/result')

def show(request):

    username = request.user.email
    post1 = Timetable1.objects.filter(username = username)
    post2 = Timetable2.objects.filter(username = username)



    return render(request, 'timetable/result.html', {'post1': post1,'post2': post2})
