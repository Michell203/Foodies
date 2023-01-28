from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home(): #home page
    if request.methods == 'POST':
        ingred1 = request.form.get('ingred1')
        provIng1 = "https://www.provigo.ca/search?search-bar="+ingred1
        r1 = requests.get(provIng1)

        soup1 = BeautifulSoup(r1.content, 'html5lib')

        price = soup1.find("span", attrs={"class":'price__value comparison-price-list__item__price__value'})

        ingred2 = request.form.get('ingred2')
        provIng2 = "https://www.provigo.ca/search?search-bar="+ingred2
        r2 = requests.get(provIng2)

        return price




    return render_template('index.html')

# @app.route("/ingreds", method = ['GET', 'POST'])
# def ingreds():
#     return render_template('ingredients.html')

if __name__ == "__main__":
    app.run()