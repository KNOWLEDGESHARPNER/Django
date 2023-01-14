from django.shortcuts import render, redirect
from django.http import HttpResponse

import student
from student.models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html')


def f1(request):
    return render(request, 'register.html')


def f2(request):
    return render(request, 'login.html')


def f3(request):
    allstudents = Student.objects.all()
    return render(request, 'showstudent.html', {'allstudents': allstudents})


def registrationfunction(request):
    userName = request.POST['name']
    userPassword = request.POST['pw']
    email = request.POST['email']
    sub = request.POST['sub']
    mob = request.POST['mob']

    s1 = Student()
    s1.name = userName
    s1.password = userPassword
    s1.email = email
    s1.subject = sub
    s1.mob = mob

    s1.save()

    return render(request, 'register.html')


def loginaction(request):
    email = request.POST['lemail']
    pw = request.POST['lpw']
    if Student.objects.filter(email=email, password=pw).exists():
        return HttpResponse('<h1>Login Success</h1>')
    else:
        return HttpResponse('<h1>Login Failure</h1>')


def updatefunction(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name= request.POST['userName']
        student.email = request.POST['userEmail']
        student.subject = request.POST['userPassword']
        student.password = request.POST['userSubject']
        student.mob = request.POST['userMobile']
        student.save()
        return redirect('show')
    return render(request, 'update.html', {'data': student})


def deletefunction(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    x = Student.objects.all()

    return render(request, 'showstudent.html', {'x': x})
