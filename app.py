from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities
import string

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home(): #home page
    if request.method == 'POST':
        ingred1 = request.form.get('ingred1')
        return utilities.parser(ingred1)
         
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run()