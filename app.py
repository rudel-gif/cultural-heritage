from flask import Flask, request, redirect, render_template, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "culturalheritage_secret"

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jadhav@1234",
    database="cultural_heritage"
)

# Landing Page
@app.route("/")
def landing():
    return render_template("home.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        try:
            cursor = db.cursor()
            sql = "INSERT INTO users (full_name, email, username, password) VALUES (%s, %s, %s, %s)"
            values = (full_name, email, username, hashed_password)

            cursor.execute(sql, values)
            db.commit()

            return redirect("/login")
        except:
            return "Registration Failed! Username may already exist."

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()
        sql = "SELECT password FROM users WHERE username=%s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[0]

            if check_password_hash(stored_password, password):
                session["username"] = username
                return redirect("/index")
            else:
                return "Invalid Username or Password"
        else:
            return "User not found"

    return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")


@app.route("/index")
def index():
    if "username" in session:
        return render_template("index.html")
    return redirect("/login")


# Static Heritage Pages
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

@app.route("/manipuri")
def manipuri():
    return render_template("manipuri.html")

@app.route("/mohiniyattam")
def mohiniyattam():
    return render_template("mohiniyattam.html")

@app.route("/odissi")
def odissi():
    return render_template("odissi.html")

@app.route("/kuchipudi")
def kuchipudi():
    return render_template("kuchipudi.html")

@app.route("/kathakali")
def kathakali():
    return render_template("kathakali.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)