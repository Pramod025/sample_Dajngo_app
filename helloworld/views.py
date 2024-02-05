from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.method=="POST":
        val1=int(request.POST['add1'])
        val2=int(request.POST['add2'])
        res=val1+val2
        return render(request,'index.html',{'result':res})
    else:
        return render(request,'index.html')



