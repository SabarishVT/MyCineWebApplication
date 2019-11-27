from flask import Flask, render_template, flash, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
debug = 1

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Sabarish'
app.config['MYSQL_PASSWORD'] = 'Promise2019'
app.config['MYSQL_DB'] = 'mycineuserdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        user_name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        country = request.form['country']
        if debug == 1:
            print(user_name)
            print(email)
            print(password)
            print(age)
            print(gender)
            print(address)
            print(phone)
            print(country)

        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO test (name, email, password) VALUES (%s,%s,%s)",(name,email,password,))
        t = (str(user_name),str(password),int(age),str(gender),str(email),str(address),int(phone),str(country))
        cur.callproc('Add_User',t)
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form['password']

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = ("SELECT * FROM user_details WHERE user_name='%s'" %(user))
        curl.execute(sql)
        user = curl.fetchone()
        print(user)
        curl.close()
        print(user)
        #Here we can implement a trigger if want
        if len(user) > 0:
            if password == user["password"]:
                session['name'] = user['user_name']
                session['email'] = user['email']
                flash('You were successfully logged in')
                return render_template("checker.html")
            else:
                flash('Password Error')
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")

@app.route('/checker',methods=["GET","POST"])
def checker():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['Gender']
        print(age)
        print(gender)
        return render_template("symptoms.html")
    else:
        return render_template("checker.html")


@app.route('/symptoms',methods=["GET","POST"])
def symptoms():
    if request.method == 'POST':
        symptoms = int(request.form['symptoms'])
        print(symptoms)
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = ("SELECT * FROM medicine_details WHERE id=%d" %(symptoms))
        curl.execute(sql)
        user = curl.fetchone()
        print(user)
        print(type(user))
        disease = user['disease']
        tablets = user['tablets']
        homeremedy = user['homeremedy']
        doctor = user['doctor']
        curl.close()
        return render_template("results.html", d=disease, t=tablets, h=homeremedy, dc=doctor)
    else:
        return render_template("symptoms.html")


@app.route('/logout')
def logout():
    session.clear()
    return render_template("home.html")

@app.route('/procedure')
def procedure():
    return render_template("procedure.html")


if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)
