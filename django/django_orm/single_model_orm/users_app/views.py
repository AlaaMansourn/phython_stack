from django.shortcuts import redirect, render
from users_app.models import Users


def index(request):
    
    all_users = Users.objects.all()

    context={"all_users":all_users}
    return render(request,'index.html',context)



def write_to_db(request):
    if request.method=='POST':
        print("it workkkkkkks")
        first_name=request.POST['first_name']
        email=request.POST['email']
        last_name=request.POST['last_name']
        age=request.POST['age']

    Users.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)
        

    return redirect("/")



# Create your views here.
