from django.shortcuts import render
from app.models import Post
from .models import Timetable1,Timetable2
from django.http import HttpResponse
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
    for day in days:
        for time in times:
            data = day + time
            listnames.append(data)
    for elemnt in tuti:
        listnames.append(elemnt)

    for day2 in listnames:
        mytime = Timetable1()
        t1 = request.POST[day2]
        if t1 == request.POST[day2] :
            if(t1 != 'null') :
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

    for day3 in listnames2:
        mytime2 = Timetable2()
        t2 = request.POST[day3]
        if t2 == request.POST[day3] :
            if(t2 != 'null') :
                mytime2.username = username
                mytime2.day = day3[2]
                mytime2.time = day3[3]
                mytime2.sub = t2
                mytime2.when = "後期"
                mytime2.save()



    return HttpResponse("run")
