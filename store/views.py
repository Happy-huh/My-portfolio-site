from django.shortcuts import render
from .models import Messages
from . import forms

# Create your views here.
def store(request):
    return render(request,'store/index.html')

def aboutMe(request):
    return render(request,'store/aboutMe.html')

def experience(request):
    return render(request,'store/experience.html')

def writeMeAMessage(request):
    if request.method == 'POST':
        form = forms.MessagesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.MessagesForm()
    return render(request,'store/writeMeAMessage.html', {'form':form})
    