from flask import Flask, request, redirect, render_template, session  # type: ignore
import mysql.connector # pyright: ignore[reportMissingImports]
from werkzeug.security import generate_password_hash, check_password_hash  # type: ignore
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
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
           return "Passwords do not match"

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

#@app.route("/logout")
#def logout():
 #   session.pop("username", None)
 #   return redirect("/")


@app.route("/index")
def index():
    if "username" in session:
        return render_template("index.html")
    return redirect("/login")

@app.route("/home")
def home():
    return render_template("home.html")

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

@app.route("/street")
def street():
    return render_template("street.html")

@app.route("/sweet")
def sweet():
    return render_template("sweet.html")

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

@app.route("/sattriya")
def sattriya():
    return render_template("sattriya.html")

@app.route("/kuchipudi")
def kuchipudi():
    return render_template("kuchipudi.html")

@app.route("/kathakali")
def kathakali():
    return render_template("kathakali.html")

@app.route("/folk")
def folk():
    return render_template("folk.html")

@app.route("/about")
def about():
    return render_template("about.html")

# TAJ MAHAL
@app.route("/tajmahal")
def tajmahal():
    return render_template("tajmahal.html")


# RED FORT
@app.route("/redfort")
def redfort():
    return render_template("redfort.html")


# QUTUB MINAR
@app.route("/qutubminar")
def qutubminar():
    return render_template("qutubminar.html")


# GATEWAY OF INDIA
@app.route("/gateway")
def gateway():
    return render_template("gatewayofindia.html")


# HAWA MAHAL
@app.route("/hawamahal")
def hawamahal():
    return render_template("hawamahal.html")


# CHARMINAR
@app.route("/charminar")
def charminar():
    return render_template("charminar.html")


# MYSORE PALACE
@app.route("/mysore")
def mysore():
    return render_template("mysore.html")


# INDIA GATE
@app.route("/indiagate")
def indiagate():
    return render_template("indiagate.html")


# KONARK SUN TEMPLE
@app.route("/suntemple")
def suntemple():
    return render_template("suntemple.html")


# GOLDEN TEMPLE
@app.route("/goldentemple")
def goldentemple():
    return render_template("goldentemple.html")


# AJANTA CAVES
@app.route("/ajanta")
def ajanta():
    return render_template("ajantacave.html")


# ELLORA CAVES
@app.route("/elloracave")
def ellora():
    return render_template("elloracave.html")


# VICTORIA MEMORIAL
@app.route("/victoriamemorial")
def victoriamemorial():
    return render_template("victoriamem.html")


# SANCHI STUPA
@app.route("/sanchistupa")
def sanchistupa():
    return render_template("sanchistupa.html")


# MEENAKSHI TEMPLE
@app.route("/meenakshi")
def meenakshi():
    return render_template("meenakshitemple.html")


# LOTUS TEMPLE
@app.route("/lotustemple")
def lotustemple():
    return render_template("lotustemple.html")


# Quiz Page
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")
#Puzzle page
@app.route("/puzzle")
def puzzle():
    return render_template("puzzle.html")

@app.route("/panjab")
def panjab():
    return render_template("panjab.html")

@app.route("/westfolk")
def westfolk():
    return render_template("westfolk.html")

@app.route("/maha")
def maha():
    return render_template("maha.html")

@app.route("/Rajs")
def Rajs():
    return render_template("Rajs.html")

@app.route("/Ass")
def Ass():
    return render_template("Ass.html")

@app.route("/gujrat")
def gujrat():
    return render_template("gujrat.html")

@app.route("/up")
def up():
    return render_template("up.html")

@app.route("/goa")
def goa():
    return render_template("goa.html")

@app.route("/kashmir")
def kashmir():
    return render_template("kashmir.html")

@app.route("/tamil")
def tamil():
    return render_template("tamil.html")


if __name__ == "__main__":
    app.run(debug=True)