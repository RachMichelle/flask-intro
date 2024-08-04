from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """""returns welcome greeting"""
    return f"<h1>Welcome</h1>"

@app.route("/welcome/home")
def welcome_home():
    """""returns welcome home greeting"""
    return f"<h1>Welcome home</h1>"

@app.route("/welcome/back")
def welcome_back():
    """""returns welcome back greeting"""
    return f"<h1>Welcome back</h1>"