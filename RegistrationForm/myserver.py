from flask import Flask,render_template,request,redirect,session,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    valid=True

    if len(request.form['firstname'])<1:
        flash('First Name field cannot be blank')
        valid=False
    elif not request.form['firstname'].isalpha():
        flash('First Name must contain only letters')
        valid=False

    if len(request.form['lastname'])<1:
        flash('Last Name field cannot be blank')
        valid=False
    elif not request.form['lastname'].isalpha():
        flash('Last Name must only contain letters')
        valid=False

    if len (request.form['email'])<1:
        flash('Email cannot be blank')
        valid=False
    elif not EMAIL_REGEX.match (request.form['email']):
        flash('Not a valid email address')
        valid=False

    if len (request.form['password'])<8:
        flash('Password must be at least 8 characters ')
        valid=False
    elif request.form['password'] != request.form['password_confirm']:
        flash ('Passwords do not match')
        valid=False

    if valid==True:
        flash('YOU DID IT!!')

    return redirect('/')

    @app.route('/reset', methods=['POST'])
    def reset():
        return redirect('/')

app.run(debug=True)
