from django.shortcuts import render
from .models import Work

# Create your views here.
def index(request):
    work_list = Work.objects.all()
    context = {
        "work_list":work_list
    }
    return render(request, "index.html", context)
