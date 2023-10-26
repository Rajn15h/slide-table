from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from.models import donermodel
from .forms import addform
# Create your views here.
def homepage(request):
    model= donermodel.objects.all()
    return render(request,'index.html',{'model':model})
def add(request):
    addforms=addform()
    if request.method=='POST':
        addforms=addform(request.POST)
        if addforms.is_valid():
            addforms.save()
            return redirect('/')
    return render(request,'add.html',{'form':addforms})


def delete(request,id):
    modela=donermodel.objects.get(id=id)
    modela.delete()
    return redirect("/")


def update(request,id):
    addmodel= donermodel.objects.get(id=id)
    addforms=addform(instance=addmodel)
    if request.method=='POST':
        addforms=addform(request.POST,instance=addmodel)
        if addforms.is_valid():
            addforms.save()
            return redirect('/add')
    return render(request,'update.html',{'addform':addforms})
