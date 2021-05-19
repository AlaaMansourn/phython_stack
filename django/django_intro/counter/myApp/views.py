from django.shortcuts import render



def display_visit(request):
    
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
    
    return render(request,'index.html')






