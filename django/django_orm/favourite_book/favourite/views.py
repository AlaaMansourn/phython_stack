from django.shortcuts import render,redirect
from favourite.models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):

    return render(request,'index.html')
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
            
            return redirect('/view_book')
        


        return redirect('/')

def login(request):
    
        if request.method=='POST':
            email= request.POST['email']
            user=User.objects.filter(email=email)


            if user:
                logged_user=user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    if 'fname' not in request.session:
                
                        request.session['fname']=logged_user.first_name
                        request.session['lname']=logged_user.last_name
                        request.session['user-id']=logged_user.id
                        print(request.session['fname'])
                        print(request.session['user-id'])
                    messages.success(request,'succesfully login')
                 
                    return redirect('/view_book')

                else:
                    messages.error(request,"login fail ")
            else: 

                messages.error(request,"No such user exist !!")
    
    
        
        
            
        return redirect('/')
        





def addbook(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        this_user=User.objects.get(id=request.session['user-id'])
        this_book=Book.objects.create(title=title,desc=desc,uploaded_by=this_user)
        this_book.user_who_like.add(this_user)
        this_user.fav_book.add(this_book)
        

    return redirect('/view_book')    
    

def viewbook(request):
    all_book=Book.objects.all()
    context={"all_book":all_book,"user-id":request.session['user-id']}
    return render(request,'welcome.html',context)








def logout(request):


    request.session.clear()


    return redirect('/')
    
    