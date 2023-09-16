from django.shortcuts import render
from .models import contact
# Create your views here.
def index(request):
    bf ="Send your massege for me!"
    return render(request,'index.html',{'alt': bf})
def ad(request):
        if request.method == 'POST':
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                message = request.POST['message']
                new_comm = contact(name=name,email=email,subject=subject,message=message)
                new_comm.save()
     
        bf = 'Your message has been sent. Thank you!'
        return render(request,'index.html',{'alt': bf})