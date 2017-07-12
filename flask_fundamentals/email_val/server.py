from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key= "ThisIsStillSomething5"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tryaddress', methods=['POST'])
def validate():
    print 1
    email_try = request.form['email']
    print 2
    if len(email_try) < 1:
        flash("Please enter an email adress.")
        print '3a'
        return redirect("/")

    elif not EMAIL_REGEX.match(email_try):
        flash("Please enter a valid email address.")
        print '3b'
        return redirect("/")

    else:
        new_query = "insert into addresses(email_address, created_at, updated_at) values (:validated_email,now(),now())"
        new_data = {"validated_email": email_try}
        mysql.query_db(new_query, new_data)
        session['success_email'] = email_try
        print '3c'
        return redirect("/success")


@app.route('/success')
def success():
    query = "select email_address, created_at from addresses"
    addresses = mysql.query_db(query)
    return render_template('success.html')


'''
@app.route('/update_address/<address_id>', methods=['POST'])
def update(address_id):
    query = "update addresses set first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = now() where id = :id"
    data = {
            'first_name': request.form['first_name']
            'last_name': request.form['last_name']
            'occupation': request.form['occupation']
            'id': address_id
            }

    mysql.query_db(query,data)
    return redirect('/')

@app.route('/remove_address/<address_id>', methods=['POST'])
def delete(address_id):
    query = "DELETE FROM addresses WHERE id = :id"
    data = {'id': address_id}
    mysql.query_db(query, data)
    return redirect('/')
    '''
app.run(debug=True)
