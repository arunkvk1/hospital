from django.shortcuts import render,redirect
from app1.models import tbl_hospital

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
