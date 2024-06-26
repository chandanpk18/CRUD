from django.shortcuts import render
from .models import Stdents
# Create your views here.
from django.contrib.auth.models import User
from django.db.models import Q
def welcome(request):
    return render(request,"responsive.html")
def gallery(request):
    return render(request,"galary.html")
def about(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        action = request.POST.get("action")

        if student_id and action:
            if action == "delete":
                try:
                    student = Stdents.objects.get(id=student_id)
                    student.delete()
                except Stdents.DoesNotExist:
                    pass
            elif action == "update":
                name = request.POST.get("name")
                email = request.POST.get("email")
                query = request.POST.get("query")
                try:
                    student = Stdents.objects.get(id=student_id)
                    student.name = name
                    student.email = email
                    student.query = query
                    student.save()
                except Stdents.DoesNotExist:
                    pass

    data = Stdents.objects.all()
    return render(request, 'about.html', {'data': data})

def query(request):
    if(request.method=="POST"):
        stud=Stdents()
        stud.name=request.POST['name']
        stud.email=request.POST['email']
        stud.contact=request.POST['contact']
        stud.query=request.POST['query']
        stud.save()
    return render(request,"bootstrap.html")
