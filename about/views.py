from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Work, Comment

# 첫번째 페이지
def index(request):
    work_list = Work.objects.all()
    context = {
        "work_list" : work_list
    }
    return render(request, "index.html", context)

# 회사소개 페이지(About)
def about(request):
    context = {

    }
    return render(request, "about.html", context)

# 작업 내용 (Work)
def work(request):
    context = {

    }
    return render(request, "work.html", context)

# 메인 > 컨텐츠 선택에서 보여지는 페이지(/{id})
def work_detail(request, work_id):
    # 선택된 id를 통해 컨텐츠를 불러오는 context 필요
    selected_work = Work.objects.get(id=work_id)
    # comment_list = Comment.objects.filter(work__id=work_id)
    # comment_list = selected_work.work_comment.all()
    context = {
        "selected_work" : selected_work,
        # "comment_list" : comment_list
    }

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        Comment.objects.create(
            work=selected_work,
            username=username,
            content=content
        )

        return HttpResponseRedirect("/{}/".format(work_id))
    return render(request, "work_detail.html", context)

# 연락
def contact(request):
    context = {

    }
    return render(request, "contact.html", context)
