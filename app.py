from flask import Flask, redirect, url_for, render_template
import utilities


app = Flask(__name__)

@app.route("/")
def home(): #home page
    return render_template('index.html')

@app.route("/recipe")
def recipe():
    return "the recipe lol"

if __name__ == "__main__":
    app.run()