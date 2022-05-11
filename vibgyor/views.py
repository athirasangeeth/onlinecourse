from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from.models import Registration

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        age=request.POST['age']
        details=Registration(username=username,password=password,email=email,age=age)
        details.save()
        # return redirect("table")
    return render(request, 'login.html')

def table(request):
    infodetails=Registration.objects.all()
    return render(request, 'table.html',{'info':infodetails})


# def delete(request,id):
#     Registration.objects.get(id=id).delete()
#     return redirect("table")

# def update(request,id):
#     updatedate=Registration.objects.get(id=id)
#     return render(request,'form.html',{'update':updatedata})