from flask import Flask, render_template, request, redirect, session,flash
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'FigureThisOneOut'



#
# def randomfarm():
#     session['num']=random.randrange(10,20)
# def randomcave():
#     session['num']=random.randrange(5,10)
# def randomhouse():
#     session['num']=random.randrange(2,5)
# def randomcasino():
#     session['num']=random.randrange(-50,50)
#


# @app.route('/')
# def index():
#     if 'gold_count' not in session:
#         session['gold_count'] = 0
#     if 'activity_log' not in session:
#         session['activity_log'] = []
#     return render_template('index.html')
# #
# @app.route('/farm',methods=['POST'])
# def farm():
#     randomfarm()
#     return render_template('index.html',num=session['num'])
#
# @app.route('/cave',methods=['POST'])
# def cave():
#     randomcave()
#     return render_template('index.html',num=session['num'])
#
# @app.route('/house',methods=['POST'])
# def house():
#     randomhouse()
#     return render_template('index.html',num=session['num'])
#
# @app.route('/casino',methods=['POST'])
# def casino():
#     randomcasino()
#     return render_template('index.html',num=session['num'])

@app.route('/')
def index():
    if 'gold_count' not in session:
        session['gold_count'] = 0
    if 'activity_log' not in session:
        session['activity_log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def getMoney():
    if request.form['action'] == 'farm':
        farm_add = random.randrange(10, 21)
        session['gold_count'] += farm_add
        string = "You have earned " + str(farm_add) + " golds. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(string)

    elif request.form['action'] == 'cave':
        cave_add = random.randrange(5, 11)
        session['gold_count'] += cave_add
        string = "You have earned " + str(cave_add) + " golds. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(string)

    elif request.form['action'] == 'house':
        house_add = random.randrange(2, 6)
        session['gold_count'] += house_add
        string = "You have earned " + str(house_add) + " golds. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(string)

    elif request.form['action'] == 'casino':
        casino_chance = random.randint(1, 2)
        if casino_chance == 1:
            casino_add = random.randrange(1, 51)
            session['gold_count'] += casino_add
            string = "You have earned " + str(casino_add) + " golds. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(string)
        elif casino_chance == 2:
            casino_add = random.randrange(-50,0)
            session['gold_count'] += casino_add
            string = "Entered a casino and lost " + str(casino_add) + " golds... Ouch! " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(string)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')

#
app.run(debug=True)
