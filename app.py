import pickle
from flask import Flask, render_template, request, redirect, url_for, session
from sqlite3 import *
from flask_mail import Mail, Message
from random import randrange
import os
import sqlite3

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "rahul3355"

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "flask9993@gmail.com"
app.config['MAIL_PASSWORD'] = "flask@2000"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if "username" in session:
        return render_template("home.html", name=session["username"])
    else:
        return redirect(url_for("login"))


@app.route("/check", methods=["GET", "POST"])
def check():
    us = session["username"]
    em = session["email"]

    age = int(request.args.get("age"))
    sex = int(request.args.get("sex"))
    cp = int(request.args.get("cp"))
    trestbps = int(request.args.get("trestbps"))
    chol = int(request.args.get("chol"))
    fbs = int(request.args.get("fbs"))
    restecg = int(request.args.get("restecg"))
    thalach = int(request.args.get("thalach"))
    exang = int(request.args.get("exang"))
    oldpeak = float(request.args.get("oldpeak"))
    slope = int(request.args.get("slope"))
    ca = int(request.args.get("ca"))
    thal = int(request.args.get("thal"))

    dd = []
    dd.append(age)
    dd.append(sex)
    dd.append(cp)
    dd.append(trestbps)
    dd.append(chol)
    dd.append(fbs)
    dd.append(restecg)
    dd.append(thalach)
    dd.append(exang)
    dd.append(oldpeak)
    dd.append(slope)
    dd.append(ca)
    dd.append(thal)
    print(dd)
    ddd = [dd]

    with open("heart3.model", "rb") as f:
        model = pickle.load(f)

    res = model.predict(ddd)
    res = str(res)
    p1 = int(res[1])

    answer = ""
    if p1 == 1:
        answer = "There is a heart disease present. 89% accurate."
    else:
        answer = "Heart disease not present. 89% accurate."

    msg = Message("RESULTS!!", sender="flask9993@gmail.com", recipients=[em])
    msg.body = "Hi " + str(us) + ". " + answer
    mail.send(msg)

    conf = " Email sent to " + str(em)

    connection = sqlite3.connect(currentdirectory + "/users.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO user_data2 VALUES('{age}','{sex}','{cp}','{trestbps}','{chol}','{fbs}','{restecg}','{thalach}','{exang}','{oldpeak}','{slope}','{ca}','{thal}','{target}')".format(
        age=age,
        sex=sex,
        cp=cp,
        trestbps=trestbps,
        chol=chol,
        fbs=fbs,
        restecg=restecg,
        thalach=thalach,
        exang=exang,
        oldpeak=oldpeak,
        slope=slope,
        ca=ca,
        thal=thal,
        target=p1)
    cursor.execute(query1)
    connection.commit()
    print("Entry inserted")
    connection.close()

    return render_template("home.html", msg=answer, conf=conf)


@app.route("/table", methods=["GET"])
def table():
    try:
        if request.method == "GET":
            connection = sqlite3.connect(currentdirectory + "/users.db")
            cursor = connection.cursor()
            query1 = "SELECT * FROM user_data2"
            result = cursor.execute(query1)
            result = result.fetchall()
            return render_template("table.html", data=result)
    except:
        return render_template("table.html", data=" $$ ")
    finally:
        if connection is None:
            connection.close()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        con = None
        try:
            con = connect("users.db")
            cursor = con.cursor()
            sql = "select * from user where username = '%s' and password='%s'"
            cursor.execute(sql % (un, pw))
            data = cursor.fetchall()
            print(data)

            if len(data) == 0:
                return render_template("login.html", msg="invalid login")
            else:
                session["username"] = un
                e1 = data[0]
                print(e1)
                e_mail = e1[2]
                print(e_mail)
                session["email"] = e_mail
                return redirect(url_for('home'))
        except Exception as e:
            msg = "issue " + e
            return render_template("register.html", msg=msg)
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        un = request.form["un"]
        em = request.form["em"]
        con = None
        try:
            con = connect("users.db")
            cursor = con.cursor()
            pw = ""
            text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            for i in range(8):
                pw = pw + text[randrange(len(text))]
            print(pw)
            sql = "insert into user values('%s','%s','%s')"
            cursor.execute(sql % (un, pw, em))
            con.commit()
            msg = Message("SUCCESS <3 :) Welcome to your project!!",
                          sender="flask9993@gmail.com",
                          recipients=[em])
            msg.body = "ur password is " + pw
            mail.send(msg)
            return redirect(url_for('login'))
        except Exception as e:
            print(str(e))
            con.rollback()
            return render_template("register.html",
                                   msg="user already registered")
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("register.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))


@app.route("/working")
def working():
    return render_template("working.html")


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


if __name__ == "__main__":
    app.run(debug=True)
