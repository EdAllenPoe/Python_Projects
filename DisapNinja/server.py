from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('all.html')

@app.route('/ninja/<color>')
def color(color):
    print color
    return render_template('color.html',color=color)


# @app.route('/red')
# def red():
#     return render_template('red.html')
#
# @app.route('/orange')
# def orange():
#     return render_template('orange.html')
#
# @app.route('/purple')
# def purple():
#     return render_template('purple.html')
#
# @app.route('/blue')
# def blue():
#     return render_template('blue.html')
#
# @app.route('/*')
# def all():
#     return render_template('april.html')



app.run(debug=True)
