from flask import Flask, render_template,redirect,request,session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret7'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print "This is an opening line"
    if 'log' not in session:
        session['log'] = []
        session['gold'] = 0
    currloc = request.form['building']
    if currloc =='farm':
        gold = random.randint(10,20)
    elif currloc == 'cave':
        gold = random.randint(5,10)
    elif currloc == 'house':
        gold = random.randint(2,5)
    elif currloc == 'casino':
        gold = random.randint(-50,50) 
          
    print currloc
    print gold
    print datetime.now()
    x = session['log']
    x.insert(0,(currloc,gold,datetime.now()))
    session['log'] = x
    session['gold'] += gold

    return redirect('/')

app.run(debug=True)

'''farm 10-20
cave 5-10
house2-5
casino+- 0-50
'''