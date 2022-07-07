from django.shortcuts import render, redirect
from .models import Note


def index(request):
    context={
        'notes' : Note.objects.all()
    }
    return render(request,'index.html',context)

def base(request,id):
    context={
        'note': Note.objects.get(id=id)
    }
    return render(request,'base.html',context)

def form(request):
    return render(request,'form.html')

def create(request):
    Name=request.GET['Name']
    Description = request.GET['Description']
    Note.objects.create(name=Name, description=Description)
    
    
    return redirect('form-page')

def update_form(request,id):
    context={
        'note': Note.objects.get(id=id)
    }
    
    return render(request,'updateform.html',context)

def update(request,id):
    Name=request.GET['Name']
    Description = request.GET['Description']
    note = Note.objects.get(id=id)
    note.name=Name
    note.description=Description
    note.save()
    
    return redirect('index-page')

def delete(request,id):
    Note.objects.get(id=id).delete()
    return redirect('index-page')
    
        

    
