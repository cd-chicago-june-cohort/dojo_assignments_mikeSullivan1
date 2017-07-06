from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', greeting="Howdy there")

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo_new():
    return render_template('dojos.html')
app.run(debug=True)                   
