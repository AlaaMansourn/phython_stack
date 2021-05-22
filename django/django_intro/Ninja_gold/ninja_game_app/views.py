from django.shortcuts import render, redirect, HttpResponse
import random, datetime
def index(request):
    return render(request, "index.html")

def process_money(request):
    if request.method == "POST":
        if 'count' not in request.session or 'activites' not in request.session:
            request.session['count']=0 
            request.session['activites']=[]

        if request.POST['building'] == 'farm' :
            gold = random.randint(10,20)
            request.session['count'] += gold
            request.session['activites'].append('Earned ' + str(gold) + ' golds from the farm! '+ str(datetime.datetime.now()))
            

        if request.POST['building'] == 'cave' :
            gold = random.randint(5,10)
            request.session['count'] += gold
            request.session['activites'].append('Earned ' + str(gold) + ' golds from the cave! '+ str(datetime.datetime.now()))
            

        if request.POST['building'] == 'house' :
            gold = random.randint(2,5)
            request.session['count'] += gold
            request.session['activites'].append('Earned ' + str(gold) + ' golds from the house! ' + str(datetime.datetime.now()))
            

        if request.POST['building'] == 'casino' :
            gold = random.randint(-50,50)
            result="Earned"
            if gold<0:
                result="Lost"
            request.session['count'] += gold
            request.session['activites'].append( result+ " " + str(gold) + ' golds from the casino! ' + str(datetime.datetime.now()))

        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
    

# Create your views here.
