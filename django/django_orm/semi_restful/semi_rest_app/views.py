from django.shortcuts import render,redirect
from semi_rest_app.models import Show, ShowManager
from django.contrib import messages

def index(request):
    return redirect("/shows/new")


def index1(request):
    pass
# Create your views here.
    return render(request,'index.html')


def index2(request):
    errors= Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)

        return redirect('/')


    else:
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],description=request.POST['description'])
        x=Show.objects.last()
        y=x.id
        messages.success("Success")

    return redirect('/shows/'+str(y))


def index3(request,id):
    this_show=Show.objects.get(id=id)
    context={"show":this_show}

    return render(request,'index3.html',context)




def tvShows(request):
    shows=Show.objects.all()
    context={"shows":shows}



    return render(request,'index4.html',context)


def showEdit(request,id):
    


    this_show=Show.objects.get(id=id)
    context={"this_show":this_show}

    return render(request,'editpage.html',context)

def updateShow(request):
    errors= Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)

        return redirect('/')
    else:
        id=request.POST['id']
    
        this_show=Show.objects.get(id=id)
    
        this_show.title=request.POST['title']
        this_show.network=request.POST['network']
        this_show.release_date=request.POST['release_date']
        this_show.description=request.POST['description']
        this_show.save()

    return redirect('/shows/'+str(id))

def deleteShow(request,id):

   this_show=Show.objects.get(id=id)
   this_show.delete()


   return redirect('/shows')
