from django.shortcuts import render,redirect



def display_visit(request):
    
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
    
    return render(request,'index.html')

def clear_session(request):

    request.session.clear()

    return redirect('/')




