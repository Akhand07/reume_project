from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Basicdetails, Education

# from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'userdetails/home.html')

# user Login
def handlelogin(request):
    if request.method == "POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername, password= loginpassword)
        if user is not None:
            login(request,user)
            return render(request, 'userdetails/adddetails.html')

        else:
            return redirect('home')

# Logout_page
def handlelogout(request):
        logout(request)
        return redirect('home')

        return HttpResponse('handlelogout')



def basicdetails(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        date_of_birth=request.POST['date_of_birth']
        gender = request.POST['gender']
        about = request.POST['about']
        dt = Basicdetails(first_name=first_name,last_name=last_name,father_name=father_name,mother_name=mother_name, date_of_birth=date_of_birth,gender=gender,about=about)
        dt.save()
        # messages.success(request, "Profile Created Succesfully")
    return render(request, 'userdetails/adddetails.html')

def viewbasicdetails(request):
    viewdata = Basicdetails.objects.all()
    print(Basicdetails)
    newdict = {
        "viewedudetails": viewdata
    }
    return render(request, 'userdetails/viewbasicdetails.html', newdict)


def education(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        university_name = request.POST['university_name']
        passing_year = request.POST['passing_year']
        edt = Education(course_name=course_name, university_name=university_name, passing_year=passing_year)
        edt.save()

    return render(request, 'userdetails/education.html')


def vieweducationdetails(request):
    viewdata = Education.objects.all()
    print(Education)
    datadict = {
        "viewdetails": viewdata
    }
    return render(request, 'userdetails/vieweducationdetails.html', datadict)

def editdata(request, id):
    viewdata = Education.objects.get(id=id)
    if request.method == "POST":
        course_name = request.POST['course_name']
        university_name = request.POST['university_name']
        passing_year = request.POST['passing_year']
        olddata = Education.objects.filter(id=id)
        olddata.update(course_name=course_name, university_name=university_name, passing_year=passing_year)
        return redirect('vieweducationdetails')
    print(Education)
    datadict = {
        "viewdetails": viewdata
    }
    return render(request, 'userdetails/editdetails.html', datadict)

def deletedata(request):
    if request.method == "POST":
        check = request.POST.getlist('chk')
        for id in check:
            Education.objects.get(id=id).delete()
    return redirect('vieweducationdetails')


def deleteviewdata(request):
    if request.method == "POST":
        check = request.POST.getlist('chk')
        for id in check:
            Basicdetails.objects.get(id=id).delete()

    return redirect('viewbasicdetails')

def editbasicdata(request, id):
    viewdata = Basicdetails.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        about = request.POST['about']
        newdata = Basicdetails.objects.filter(id=id)
        newdata.update(first_name=first_name,last_name=last_name,father_name=father_name,mother_name=mother_name, date_of_birth=date_of_birth,gender=gender,about=about)
        return redirect('viewbasicdetails')
    print(Education)
    newdict = {
        "viewedudetails": viewdata
    }
    return render(request, 'userdetails/editbasicdetails.html', newdict)
