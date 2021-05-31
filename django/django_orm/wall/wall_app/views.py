from django.shortcuts import render,redirect
from  wall_app.models import User,UserManager,Message,Comment
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,"index.html")

def register(request):
        if request.method=='POST':
        
            errors=User.objects.basic_validator(request.POST)
            if len(errors)>0:
                for key,value in errors.items():
                    messages.error(request,value)
                return redirect('/login')
        
            else:
                first_name=request.POST['fname']
                last_name=request.POST['lname']
                email=request.POST['email']
                password=request.POST['password']
                pw=request.POST['pw']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)

            if 'first_name' not in request.session:
                request.session['first_name']=request.POST['fname']
                request.session['last_name']=request.POST['lname']
                request.session['email']=request.POST['email']
                request.session['password']=request.POST['password']
                messages.success(request,"succefully register")
            
            return redirect('/success')
        


        return redirect('/login')


def login(request):
    
        if request.method=='POST':
            email= request.POST['email']
            user=User.objects.filter(email=email)


            if user:
                logged_user=user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    if 'fname' not in request.session:
                
                        request.session['fname']=logged_user.first_name
        
                    messages.success(request,'succesfully login')
                 
                    return redirect('/success')

                else:
                    messages.error(request,"login fail ")
            else: 

                messages.error(request,"No such user exist !!")
    
    
        else:
            return render(request,'index.html')
            
        return redirect('/login')
        


def success(request):

    return render (request,'success.html')


def logout(request):

    request.session.clear()

    return redirect('/')


def wall(request):
    
    if request.method=='POST':
        # email=request.session['email']
        # print(email)
        # print("nowwwwwwwwwwwwww")
        # text = request.POST['messagetext']
        

    all_messages=Message.objects.all()
       
       
       
    context={"all_messages":all_messages}

    

    return render(request,'wall.html',context)

# Create your views here.
