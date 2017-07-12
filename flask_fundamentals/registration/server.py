from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'registration')
app.secret_key= "ThisIsStillSomething6"

#hashed_pass = md5.new(password).hexdigest()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    error=None
    new_user=False
    if request.form['auth_type']=='register':
        new_user = True
    email = request.form['email']
    print email
    password = request.form['password']
    print password
    if new_user:
        first_name = request.form['first_name']
        print first_name
        last_name = request.form['last_name']
        print last_name
        confirm = request.form['confirm']
        print confirm


    select_user = "SELECT * FROM registration.users where email = :email"
    variables = {"email":email}
    get_email = mysql.query_db(select_user,variables)
    print '-'*50, get_email

    if new_user:
        if len(get_email) > 0:
            flash("This user is already registered. You should Log in instead of registering.")
            error = True
            
        else:
            if not EMAIL_REGEX.match(email):
                flash("Need a Valid Email to Register")
                print "Please Enter A Valid Email Address"
                error = True
            if not first_name.isalpha() or len(first_name) < 2 :
                flash("Please Enter A Valid First Name")
                print "Please Enter A Valid First Name"
                error = True

            if not last_name.isalpha() or len(last_name) < 2:
                flash("Need a Valid Last Name to Register")
                print "Please Enter A Valid Last Name"
                error = True
            
            if len(password) < 8:
                flash("Please Enter A Longer Password")
                print "Please Enter A Longer Password"
                error = True

            if password != confirm:
                flash("Passwords do not match")
                print "Passwords do not match"
                error = True
    else:
        if not EMAIL_REGEX.match(email):
            flash("This user is not registered")
            print "This user is not registered"
            error = True
        if get_email[0]['pass'] != md5.new(password).hexdigest():
            print md5.new(password).hexdigest()
            print get_email[0]["pass"]
            flash("This Password is incorrect")
            print "This Password is incorrect"
            error = True
            
    
    if error:
        return redirect("/")
    else:
        if new_user:
            hashed_pass = md5.new(password).hexdigest()
            insert_user = "INSERT INTO users (first_name, last_name,email, pass, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now());"
            insert_vars = {"email":email, "first_name": first_name, "last_name":last_name,"password": hashed_pass }
            get_email = mysql.query_db(insert_user,insert_vars)
        session['email'] = email
        return redirect("/success")
    
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
