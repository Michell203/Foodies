from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities

app = Flask(__name__)

@app.route("/", method = ['GET', 'POST'])
def home(): #home page
    if request.method == 'POST':
        ingred1 = request.form.get('ingred1')
        provIng1 = "https://www.provigo.ca/search?search-bar="+ingred1
        r1 = requests.get(provIng1)

        ingred2 = request.form.get('ingred2')
        provIng2 = "https://www.provigo.ca/search?search-bar="+ingred2
        r2 = requests.get(provIng2)




    return render_template('index.html')

# @app.route("/ingreds", method = ['GET', 'POST'])
# def ingreds():
#     return render_template('ingredients.html')

if __name__ == "__main__":
    app.run()