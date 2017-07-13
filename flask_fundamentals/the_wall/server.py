from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime, timedelta
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')
app.secret_key= "ThisIsStillSomething201"

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
    password = request.form['password']
    if new_user:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        confirm = request.form['confirm']
        

    select_user = "SELECT * FROM the_wall.users where email = :email"
    variables = {"email":email}
    get_email = mysql.query_db(select_user,variables)
    
    if new_user:
        if len(get_email) > 0:
            flash("This user is already registered. You should Log in instead of registering.")
            error = True
            
        else:
            if not EMAIL_REGEX.match(email):
                flash("Need a Valid Email to Register")
                error = True
            if not first_name.isalpha() or len(first_name) < 2 :
                flash("Please Enter A Valid First Name")
                error = True

            if not last_name.isalpha() or len(last_name) < 2:
                flash("Need a Valid Last Name to Register")
                error = True
            
            if len(password) < 8:
                flash("Please Enter A Longer Password")
                error = True

            if password != confirm:
                flash("Passwords do not match")
                error = True
    else:
        if not EMAIL_REGEX.match(email):
            flash("This user is not registered")
            error = True
        if get_email[0]['password'] != md5.new(password).hexdigest():
            flash("This Password is incorrect")
            error = True
            
    
    if error:
        return redirect("/")
    else:
        if new_user:
            hashed_pass = md5.new(password).hexdigest()
            insert_user = "INSERT INTO users (first_name, last_name,email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now());"
            insert_vars = {"email":email, "first_name": first_name, "last_name":last_name,"password": hashed_pass }
            session['id'] = mysql.query_db(insert_user,insert_vars)
            session['first_name'] = first_name
            session['last_name'] = last_name
        else:
            session['first_name'] = get_email[0]["first_name"]
            session['last_name'] = get_email[0]["last_name"]
            session['id'] = get_email[0]["id"]
        session['email'] = email
        return redirect("/wall")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def success():
    select_msgs_str = "select message, messages.id as message_id, users.id as user_id, users.first_name, users.last_name, messages.created_at from users, messages where user_id = users.id order by messages.created_at desc"
    select_msgs = mysql.query_db(select_msgs_str)
    select_comm_str = "select comments.id as comment_id, comments.message_id, users.id as user_id, users.first_name, users.last_name, comments.comment, comments.created_at from users, comments where comments.user_id =users.id"
    select_comm = mysql.query_db(select_comm_str)
    print datetime.now()- timedelta(minutes=30)
    
    return render_template('wall.html', all_msgs = select_msgs, all_comm = select_comm)

@app.route('/new_message', methods = ['POST'])
def add_new_mess():
    message = request.form['message']
    insert_var = { "message":message, "user_id":session['id'] }
    insert_str = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message,now(),now())"
    insert_msg = mysql.query_db(insert_str,insert_var)
    return redirect('/wall')

@app.route('/new_comment', methods = ['POST'])
def add_new_comment():
    comment = request.form['comment']
    message_id = request.form['message_id']
    insert_comm_var = { "comment":comment, "user_id":session['id'], "message_id":message_id }
    insert_comm_str = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id,:comment,now(),now())"
    insert_comm_msg = mysql.query_db(insert_comm_str,insert_comm_var)
    return redirect('/wall')

@app.route('/delete_comment/<comment_id>', methods = ['POST'])
def delete_comment(comment_id):
    delete_comm_var = {"comment_id": comment_id}
    delete_comm_str = "delete from comments where id = :comment_id"
    mysql.query_db(delete_comm_str,delete_comm_var)
    return redirect('/wall')

@app.route('/delete_message/<message_id>', methods = ['POST'])
def delete_message(message_id):
    delete_msgcomm_var = {"message_id": message_id}
    delete_msgcomm_str = "delete from comments where message_id = :message_id"
    mysql.query_db(delete_msgcomm_str,delete_msgcomm_var)
    delete_msg_var = {"message_id": message_id}
    delete_msg_str = "delete from messages where id = :message_id"
    mysql.query_db(delete_msg_str,delete_msg_var)

    
    return redirect('/wall')

app.run(debug=True)
