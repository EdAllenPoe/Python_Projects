# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['firstname'])<1:
        flash('First Name field cannot be blank')
    elif not request.form['firstname'].isalpha():
        flash('First Name must contain only letters')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['lastname'])<1:
        flash('Last Name field cannot be blank')
    elif not request.form['lastname'].isalpha():
        flash('Last Name must only contain letters')
    if len (request.form['password'])<8:
        flash('Password must be at least 8 characters ')
    elif request.form['password'] != request.form['password_confirm']:
        flash ('Passwords do not match')
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
