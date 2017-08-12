from flask import Flask, render_template, request, redirect, session, flash, url_for
import os
import unicodedata

app = Flask(__name__)
app.secret_key = 'HolySecretCode'

def countLetters(word):
    count = 0
    for c in word:
        count += 1
    return count

@app.route('/')
def index():
    option_list = ['San Jose', 'New York', 'Seattle']
    language_list = ['Python', 'PHP', 'Javascript']
    return render_template('index.html', option_list=option_list, language_list=language_list)
@app.route('/create', methods=['POST'])
def create_user():
    if request.form['name'] == '' and request.form['comment'] == '':
        flash('Name cannot be blank', 'nameError')
        flash('Comment cannot be blank', 'commentError')
        return redirect('/')
    if request.form['name'] == '':
        flash('Name cannot be blank', 'nameError')
        return redirect('/')
    if request.form['comment'] == '':
        flash('Comment cannot be blank', 'commentError')
        return redirect('/')
    session['comment'] = request.form['comment']
    comment = countLetters(session['comment'])
    print (comment)
    if comment > 120:
        flash('Comment cannot be more than 120 characters', 'commentError')
        return redirect('/')

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return redirect('/process')

@app.route('/process')
def show_user():
    return render_template('results.html')

app.run(debug=True)
