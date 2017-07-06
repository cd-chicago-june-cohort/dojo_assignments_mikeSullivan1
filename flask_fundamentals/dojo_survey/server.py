from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process():
    user_name=request.form['user_name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    return render_template('result.html', result_name = user_name,result_location=location,result_language = language,result_comment = comment)

app.run(debug=True)                   
