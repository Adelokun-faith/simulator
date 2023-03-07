from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
 
app = Flask(__name__)
 
 
app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)


@app.route('/')
@app.route('/home', methods =['GET', 'POST'])
def home():
    msg = ''
    if request.method == 'POST' and 'fname' in request.form and 'fame' in request.form and 'party' in request.form and 'lag' in request.form and 'name' in request.form and 'hote' in request.form and 'fro' in request.form :
        fname = request.form['fname']
        fame = request.form['fame']
        party = request.form['party']
        lag = request.form['lag']
        name = request.form['name']
        hote = request.form['hote']
        fro = request.form['fro']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM vote WHERE fname = % s', (fname, fame, party, lag, name, hote, fro))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', fname):
            msg = 'fname must contain only characters and numbers !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', fame):
            msg = 'Invalid DOB address !'
        elif not re.match(r'[A-Za-z0-9]+', party):
            msg = 'invalid mobile !'
        elif not re.match(r'[A-Za-z0-9]+', lag):
            msg = 'invalid mobile !'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'invalid mobile !'
        elif not re.match(r'[A-Za-z0-9]+', hote):
            msg = 'invalid mobile !'
        elif not re.match(r'[A-Za-z0-9]+', fro):
            msg = 'invalid mobile !'
        else:
            cursor.execute('INSERT INTO vote VALUES (% s, % s, % s, % s, % s, % s, % s)', (fname, fame, party, lag, name, hote, fro))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('home.html',msg=msg)


        



        
        
        
        
if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')