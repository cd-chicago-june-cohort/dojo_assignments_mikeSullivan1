from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
@app.route('/')
def index():
    query = "select name,age, month(created_at) as month, day(created_at) as day,year(created_at) as year from friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', all_friends = friends)

'''@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "select * from friends where id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query,data)
    return render_template('index.html',one_friend = friends[0])
'''
@app.route('/friends', methods=['POST'])
def create():
    query = "insert into friends(name, age, created_at, updated_at) values (:name, :age, now(), now())"
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
    }
    mysql.query_db(query,data)
    return redirect('/')
'''
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "update friends set first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = now() where id = :id"
    data = {
            'first_name': request.form['first_name']
            'last_name': request.form['last_name']
            'occupation': request.form['occupation']
            'id': friend_id
            }

    mysql.query_db(query,data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')
    '''
app.run(debug=True)
