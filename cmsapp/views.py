from django.shortcuts import render, redirect
from .models import DepartmentModel
from .forms import DepartmentForm
from .models import StudentModel
from .forms import StudentForm
from .models import SportModel
from .forms import SportForm
from .models import InfoModel
from .forms import InfoForm

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def showdept(request):
    data= DepartmentModel.objects.all()
    return render(request,'showdept.html',{'data':data})
    
def adddept(request):
    if request.method == "POST":
        f = DepartmentForm(request.POST)
        if f.is_valid():
            f.save()
            fm = DepartmentForm()
            return render(request,'adddept.html',{'fm':fm, 'msg':'Department Added'})
        else:
            return render(request,'adddept.html',{'fm':f, 'msg':'Check Errors'})
    else:
        fm = DepartmentForm()
        return render(request,'adddept.html',{'fm':fm})
        
def deletedept(request,id):
    d= DepartmentModel.objects.get(deptid=id)
    d.delete()
    return redirect('showdept')
    
def showstudent(request):
    data=StudentModel.objects.all()
    return render(request,'showstudent.html',{'data':data})

def addstudent(request):
    if request.method=="POST":
        f= StudentForm(request.POST)
        if f.is_valid():
            f.save()
            fm=StudentForm()
            return render(request,'addstudent.html',{'fm':fm,'msg':'Record saved'})
        
        else:
            return render(request,'addstudent.html',{'fm':f,'msg':'Check errors'})
    
    else:
        fm=StudentForm()
        return render(request,'addstudent.html',{'fm':fm})

def deletestudent(request,id):
    d= StudentModel.objects.get(rno=id)
    d.delete()
    return redirect('showstudent')

def showsport(request):
    data = SportModel.objects.all()
    final_data = []
    for d in data:
        sportstudent = d.student.all()
        for student in sportstudent:
            tempdict = {
                "sportid" : d.sportid,
                "name": d.sportname,
                "studentname": student.name
            }
            final_data.append(tempdict)
    return render(request,'showsport.html',{'data':final_data})

def addsport(request):
    if request.method=="POST":
        f= SportForm(request.POST)
        if f.is_valid():
            f.save()
            fm=SportForm()
            return render(request,'addsport.html',{'fm':fm,'msg':'Record saved'})
        
        else:
            return render(request,'addsport.html',{'fm':f,'msg':'Check errors'})
    
    else:
        fm=SportForm()
        return render(request,'addsport.html',{'fm':fm})

def deletesport(request,id):
    d= SportModel.objects.get(sportid=id)
    d.delete()
    return redirect('showsport')

def showinfo(request):
    
    data = InfoModel.objects.all()
    final_data = []
    for d in data:
        tempdict = {
            "rollno":d.student.rno,
            "studentname": d.student.name,
            "mobile" : d.mobile,
            "address": d.address
            }
        final_data.append(tempdict)
    return render(request,'showinfo.html',{'data':final_data})

def addinfo(request):
    if request.method=="POST":
        f= InfoForm(request.POST)
        if f.is_valid():
            f.save()
            fm=InfoForm()
            return render(request,'addinfo.html',{'fm':fm,'msg':'Record saved'})
        
        else:
            return render(request,'addinfo.html',{'fm':f,'msg':'Check errors'})
    
    else:
        fm=InfoForm()
        return render(request,'addinfo.html',{'fm':fm})

def deleteinfo(request,id):
    d= InfoModel.objects.get(info=id)
    d.delete()
    return redirect('showinfo')