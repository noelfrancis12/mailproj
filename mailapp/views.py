from django.shortcuts import render,redirect
from mailapp.models import Student
from mailapp.forms import studentforms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def add(request):
    form=studentforms()
    return render(request,'add.html',{'form':form})
def sndmail(request):
    if request.method=="POST":
        form=studentforms(request.POST)
        if form.is_valid():
            form.save()
            subject="Application for python developer"
            message="We have received your application for thepost of software developer.Thank you."
            recepient=form.cleaned_data.get('Email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recepient])
            return redirect('/')
        return render(request,'add.html')