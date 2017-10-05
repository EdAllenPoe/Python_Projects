from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, 'ninjagoldapp/index.html')

def getMoney(request):
    if request.POST['action'] == 'farm':
        farm_add = random.randrange(10, 21)
        request.session['gold_count'] += farm_add
        string = "You have earned " + str(farm_add) + " golds from the farm. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'cave':
        cave_add = random.randrange(5, 11)
        request.session['gold_count'] += cave_add
        string = "You have earned " + str(cave_add) + " golds from the cave. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'house':
        house_add = random.randrange(2, 6)
        request.session['gold_count'] += house_add
        string = "You have earned " + str(house_add) + " golds from the house. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'casino':
        casino_chance = random.randint(1,2)
        if casino_chance == 1:
            casino_add = random.randrange(1, 50)
            request.session['gold_count'] += casino_add
            string = "You have earned " + str(casino_add) + " golds from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity_log'].append(string)
        elif casino_chance == 2:
            casino_add = random.randint(-50,0)
            request.session['gold_count'] += casino_add
            string = "Entered a casino and lost " + str(casino_add) + " golds... Ouch! " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity_log'].append(string)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
