from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rudrayani@123",
    database="cultural_heritage"
)

cursor = db.cursor()

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Register
# Show Register Page (GET)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        sql = "INSERT INTO users (full_name, email, username, password) VALUES (%s, %s, %s, %s)"
        values = (full_name, email, username, password)

        cursor.execute(sql, values)
        db.commit()

        return redirect("/index")

    return render_template("register.html")


# Login
# Show Login Page (GET) and Handle Login (POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        values = (username, password)

        cursor.execute(sql, values)
        user = cursor.fetchone()

        if user:
            return redirect("/index")
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


@app.route("/festivals")
def festivals():
    return render_template("festivals.html")

@app.route("/classicaldance")
def classicaldance():
    return render_template("classicaldance.html")

@app.route("/foods")
def foods():
    return render_template("foods.html")

@app.route("/monuments")
def monuments():
    return render_template("monuments.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/traditions")
def traditions():
    return render_template("traditions.html")

@app.route("/diwali")
def diwali():
    return render_template("diwali.html")

@app.route("/dussehra")
def dussehra():
    return render_template("dussehra.html")

@app.route("/holi")
def holi():
    return render_template("holi.html")

@app.route("/janmashtami")
def janmashtami():
    return render_template("janmashtami.html")

@app.route("/navratri")
def navratri():
    return render_template("navratri.html")

@app.route("/pongal")
def pongal():
    return render_template("pongal.html")

@app.route("/raksha")
def raksha():
    return render_template("raksha.html")

@app.route("/sankranti")
def sankranti():
    return render_template("sankranti.html")

@app.route("/chaturthi")
def chaturthi():
    return render_template("chaturthi.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/west")
def west():
    return render_template("west.html")

@app.route("/east")
def east():
    return render_template("east.html")

@app.route("/north")
def north():
    return render_template("north.html")

@app.route("/south")
def south():
    return render_template("south.html")

@app.route("/kathak")
def kathak():
    return render_template("kathak.html")

@app.route("/bharatnatyam")
def bharatnatyam():
    return render_template("bharatnatyam.html")

if __name__ == "__main__":
    app.run(debug=True)