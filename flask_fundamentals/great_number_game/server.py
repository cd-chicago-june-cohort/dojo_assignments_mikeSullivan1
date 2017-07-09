from flask import Flask, render_template,redirect,request,session
import random

app = Flask(__name__)
app.secret_key = 'changes23457789123'

@app.route('/')
def index():
    if 'rando' not in session:
        session['rando'] = random.randrange(0,101)
        session['guess'] = 'None'
    print type(session['guess'])
    return render_template('index.html',random = session['rando'],guess = session['guess'])

@app.route('/eval', methods = ['POST'])
def eval():
    if request.form['guess']:
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)