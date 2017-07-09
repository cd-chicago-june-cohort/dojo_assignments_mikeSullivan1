from flask import Flask, render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'changes234'

@app.route('/')
def index():
    if 'y' not in session:
        session['y'] = 0
    session['y']+= 1  
    return render_template('index.html')

@app.route('/plustwo')
def redir():
    if 'y' not in session:
        session['y'] = 0
    session['y']+= 1  
    return redirect('/')

@app.route('/reset')
def reset():
    session['y'] = 0  
    return redirect('/')

app.run(debug=True)