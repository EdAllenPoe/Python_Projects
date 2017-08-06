from flask import Flask, render_template,request,redirect

app=Flask(__name__)

@app.route('/')
def dojosurvey():
    return render_template('dojosurvey.html')



@app.route('/users', methods=['POST'])
def users():
   return render_template ("users.html",name = request.form['name'], location = request.form['location'],
                            language=request.form['language'], comment=request.form['comment'])

   # return redirect('/')

app.run(debug=True)
