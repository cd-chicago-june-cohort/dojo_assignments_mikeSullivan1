from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    red = 255
    green = 255
    blue = 255
    if request.method == 'POST':
        red=request.form['red']
        green=request.form['green']
        blue=request.form['blue']
    
    return render_template('/index.html', red=red, green=green, blue=blue)

app.run(debug=True)                   
