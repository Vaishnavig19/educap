from django.shortcuts import render, redirect
from .models import Student
from adminmodule.models import Admins,Course,Notes,Assignment,Video


# Create your views here.
def homes(request):
    try:
        if request.session['userid'] != "":
            return redirect('../')
        else:
            return redirect('../')
    except:
        return redirect('../')



def signup(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        semail = request.POST['semail']
        smobile = request.POST['smobile']
        password = request.POST['spassword']
        print(semail, password, sname, smobile)
        user = Student(sname=sname, semail=semail, smobile=smobile, password=password)
        user.save()
        return redirect('../')
    return redirect('../')



def login(request):
    if request.method == "POST":
        e = request.POST['email']
        pas = request.POST['pas']
        try:
            user = Student.objects.get(semail=e, password=pas)
            request.session['userid'] = user.id
            return redirect("../student/")
        except:
            return redirect("../")
    return redirect("../")


def logout(request):
    try:
        del request.session['userid']
        return redirect('../')
    except:
        return redirect("../")

# def files(request):
#     # try:
#         data = request.GET['data']
#         c = Course.objects.get(pk=data)
#         f = File.objects.filter(cid=c,status="active")
#         params = {'course': c,"files":f}
#         return render(request,'student/files.html',params)
#     # except:
#     #     return redirect('../student/course')
 
def course(request):
    courses=Course.objects.filter(status="active")
    print(course)
    return render(request,'student/course.html',{'courses':courses})  

def assign(request):
    try:
        data = request.GET['data']
        c = Course.objects.get(pk=data)
        a = Assignment.objects.filter(cid=c,status="active")
        params = {'course': c,"a":a}
        return render(request,'student/assign.html',params)
    except:
        return redirect('../student/course')
    return render(request,'student/assign.html')
def show(request):
    return render(request,'student/show.html')
def video(request):
    try:
        data= request.GET['data']
        c = Course.objects.get(pk=data)
        v = Video.objects.filter(cid=c,status="active")
        params = {'course': c,"v":v}
        return render(request,'student/video.html',params)
    except:
        return redirect('../student/course')
    
   
def notes(request):
    try:
        data= request.GET['data']
        c = Course.objects.get(pk=data)
        n = Notes.objects.filter(cid=c,status="active")
        print(n)
        params = {'course': c,"n":n}
        return render(request,'student/notes.html',params)
    except:
        return redirect('../student/course')
    





