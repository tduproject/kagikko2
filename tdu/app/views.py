import csv
from io import TextIOWrapper, StringIO
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from .models import Post
from polls.models import Poll ,Choice


class IndexView(generic.ListView):
    model = Post


def csv_import(request):
    q_array = ['q1','q2','q3']
    form_data = TextIOWrapper(
        request.FILES['csv'].file, encoding='utf-8')
    if form_data:
        csv_file = csv.reader(form_data)
        for line in csv_file:
            post, _ = Post.objects.get_or_create(pk=line[0])
            post.title = line[1]
            post.text = line[2]
            post.sub = line[3]
            mypoll = Poll()
            mypoll.subname = line[3]
            mypoll.question1 = "課題の難易度 "
            mypoll.question2 = "テストの難易度 "
            mypoll.question3 = "課題の量 "


            for q in q_array:
                mychoice = Choice()
                mychoice.subname = line[3]
                mychoice.value = q
                mychoice.save()

            # category, _ = Category.objects.get_or_create(name=line[4])
            post.category = line[4]
            post.when = line[5]
            post.save()
            mypoll.save()

    return redirect('app:index')


def csv_export(request):
    memory_file = StringIO()
    writer = csv.writer(memory_file)
    for post in Post.objects.all():
        row = [post.pk, post.title, post.text, post.sub, post.category,post.when]
        writer.writerow(row)
    response = HttpResponse(
        memory_file.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=db.csv'
    return response
