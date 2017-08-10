from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'




def randomnumber():
    session['num']=random.randrange(1,100)



@app.route('/')
def index():
    try:
        session['num']
    except KeyError:
        randomnumber()
    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guess():

    # num=random.randrange(1,100)

    # num=session['num']
    return render_template('guess.html',guess=int(request.form['guess']),num=session['num'])
#
app.run(debug=True)
