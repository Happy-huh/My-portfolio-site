from django.shortcuts import render, redirect
from .models import Messages, Project
from . import forms

# Create your views here.
def store(request):
    return render(request,'store/index.html')

def aboutMe(request):
    return render(request,'store/aboutMe.html')

def experience(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request,'store/experience.html', context)

def writeMeAMessage(request):
    if request.method == 'POST':
        form = forms.MessagesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = forms.MessagesForm()
        return render(request,'store/writeMeAMessage.html', {'form':form})
    