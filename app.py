import pickle
from flask import Flask, render_template, request, redirect, url_for, session
from sqlite3 import *
import os
import sqlite3

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = "rahul3355"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/check", methods=["GET", "POST"])
def check():

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
        target=p1,
    )
    cursor.execute(query1)
    connection.commit()
    print("Entry inserted")
    connection.close()

    return render_template("home.html", msg=answer)


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
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def signup():
    return render_template("home.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    return redirect(url_for("login"))


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
