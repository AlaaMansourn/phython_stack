from typing import ContextManager
from django.shortcuts import render

def display(request):

    return render(request,'index.html')

def final(request):

    name=request.POST['name']
    location=request.POST['location']
    language=request.POST['language']
    optional=request.POST['optinal']


    

    context = {

     "name" :name,"location":location,"language":language,"optional":optional}
    


    return render(request,'result.html',context)
