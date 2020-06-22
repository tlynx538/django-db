from django.shortcuts import render,redirect
from .models import Member
from .forms import memberforms
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html',{})
    
def join(request):
    if(request.method=="POST"):
        form=memberforms(request.POST or None)
        if(form.is_valid()):
            form.save()
        else:
            messages.error(request,("There was an error. Please try again Later"))  
            return redirect('join')  
        messages.success(request,("Details successfully added"))        
        return redirect('home')    
    else:
        return render(request,'join.html',{})

def members(request):
    membersx=Member.objects.all
    return render(request,'members.html',{'members':membersx})    

