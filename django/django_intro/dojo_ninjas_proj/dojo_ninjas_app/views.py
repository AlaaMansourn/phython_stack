from django.http import request
from django.shortcuts import redirect, render
from dojo_ninjas_app.models import *
def index(request):
    all_dojos = Dojo.objects.all()
    
        
    context={"dojos":all_dojos}
    
    return render(request,'index.html',context)

def addNinja(request):
    if request.method == 'POST':
        if request.POST['form1']=='ninja':
            dn=request.POST['ctninja']
            fn=request.POST['fname']
            ln=request.POST['lname']

            this_dojo=Dojo.objects.get(name=dn)
        
        
            Ninja.objects.create(dojo=this_dojo,first_name=fn,last_name=ln)
        
    return redirect("/")

def adddojo(request):
    if request.method=='POST':
        if request.POST['form1']=='dojo':
            n=request.POST['name']
            c=request.POST['city']
            s=request.POST['state']

            
            
            Dojo.objects.create(name=n,city=c,state=s)
            
    return redirect("/")


def test(request):

    return render(request,'test.html')




