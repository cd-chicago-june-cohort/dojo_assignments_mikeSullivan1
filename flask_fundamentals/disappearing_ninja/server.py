from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/')
def ninja():
    return render_template('ninja.html', template_color ="All")

@app.route('/ninja/<vararg>')
def ninja1(vararg):
    ninja_color=vararg
    return render_template('ninja.html',template_color = ninja_color)

app.run(debug=True)                   
