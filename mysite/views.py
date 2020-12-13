# I have created this file
from  django.http import  HttpResponse
from  django.shortcuts import render, redirect

# method 1 direct text
# def homepage(request):
#     return HttpResponse("Ye hai mera homepage")

# method 2nd using html
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    name = request.POST.get('formname')
    email = request.POST.get('formemail')
    subject = request.POST.get('formsubject')
    message = request.POST.get('formmessage')
    print(name)
    print(email)
    print(subject)
    print(message)
    return render(request, 'contact.html')

def platform_youtube(reqest):
    return render(reqest,'youtube.html')
