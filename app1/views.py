from django.shortcuts import render,redirect
from app1.models import tbl_hospital,tbl_patient

# Create your views here.
def index(request):
    return render(request,"index.html")
def admin1(request):
    return render(request,'admin1.html')
def adddoctor(request):
    return render(request,'adddoctor.html')
def doct(request):
    p1=tbl_hospital()
    p1.Emp_id=request.POST.get('Drid')
    p1.Doctor=request.POST.get('doc')
    p1.Specialization=request.POST.get('spec')
    p1.Salary=request.POST.get('salary')
    p1.Experience=request.POST.get('exp')
    p1.Age=request.POST.get('age')
    p1.Gender=request.POST.get('gender')
    p1.save()
    return render(request,'index.html')
def viewdoctor(request):
    data=tbl_hospital.objects.all()
    return render(request,'viewdoctor.html',{'x':data})
def deletedoctor(request,id):
    data=tbl_hospital.objects.get(id=id)
    data.delete()
    return redirect('/viewdoctor')

def patient(request):
    return render(request,'patient.html')

def addpatient(request):
    return render(request,'addpatient.html')

def link1(request):
    p2=tbl_patient()
    p2.name=request.POST.get('name')
    p2.age=request.POST.get('age')
    p2.phone=request.POST.get('ph')
    p2.email=request.POST.get('mail')
    p2.date=request.POST.get('date')
    p2.gender=request.POST.get('gender')
    p2.save()
    return render(request,'index.html')

def viewdoctor1(request):
    data1= tbl_hospital.objects.all()
    return render(request,'viewdoctor1.html',{'y':data1})

def viewprofile(request):
    data2 = tbl_patient.objects.all()
    return render(request,'viewprofile.html',{'x':data2})

def updateprofile(request,id):
    data2 = tbl_patient.objects.get(id=id)
    return render(request,'update.html',{'x':data2})

def link2(request,id):
    p2=tbl_patient.objects.get(id=id)
    p2.name=request.POST.get('name')
    p2.age=request.POST.get('age')
    p2.phone=request.POST.get('ph')
    p2.email=request.POST.get('mail')
    p2.date=request.POST.get('date')
    p2.gender=request.POST.get('gender')
    p2.save()
    return redirect('viewprofile')


def deleteprofile(request,id):
    data3=tbl_patient.objects.get(id=id)
    data3.delete()
    return redirect('/viewprofile')




















    


