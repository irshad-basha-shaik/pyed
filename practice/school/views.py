from django.shortcuts import render
from django.http import HttpRequest
from .models import Registration
from .forms import RegistrationForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def saveform(request):
    res = Registration.objects.all()
    if request.method == 'POST':
        reg = Registration( name=request.POST['name'], fname = request.POST['fname'], email = request.POST['email'], contact = request.POST['contact'])
        reg.save()
        return render(request,"studentdetails.html",{"form_list": res})
def sedit(request):
    id = request.GET['id']
    d = Registration.objects.get(id=id)
    return render(request, "sedit.html", {"form":d})

def seditform(request):
    info = Registration.objects.all()
    d = Registration.objects.filter(id=request.POST['id']).update(name=request.POST['name'], email=request.POST['email'],fname=request.POST['fname'], contact=request.POST['contact'])
    return render(request, "studentdetails.html",{"form_list":info})
def delete(request):
    info = Registration.objects.all()
    id = request.GET['id']
    d = Registration.objects.filter(id=request.GET['id']).delete()
    return render(request, "studentdetails.html",{"form_list":info})
