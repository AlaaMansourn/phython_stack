from django.shortcuts import render
import random

number = random.randint(1,100)
def index(request):
    context={}
    if request.method=='POST':
        if int( request.POST['num'])>0 and int(request.POST['num'])<100:
        
            if 'num' not in request.session:
                request.session['num']=random.randint(1,100)
            
            
            
            if int(request.session['num'])==int(request.POST['num']):
                result="you won"
                

            elif int(request.session['num']) > int(request.POST['num']):
                result="too low" 
            elif int(request.session['num']) < int(request.POST['num']):
                result="too high"
    
            context={"first":request.session['num'],"second":request.POST['num'],"result":result} 
            
    return render(request,'index.html',context)
    
# Create your views here.
