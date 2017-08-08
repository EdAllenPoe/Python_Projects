from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
counter = 0

def Sessions():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


@app.route('/')
def index():
    Sessions()
    session['counter'] = session['counter']
    return render_template('index.html', counter=session['counter'])

app.run(debug=True)
