from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<vararg>')
def ninja1(vararg):
    if vararg not in ["purple","blue","orange","red"]:
        return render_template('notapril.html')
    string = vararg+'.html'
    return render_template(string)

app.run(debug=True)                   
