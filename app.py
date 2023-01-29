from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home(): #home page
    if request.method == 'POST':
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        ingred1 = request.form.get('ingred1')
        ingIngred = "https://www.iga.net/en/search?t={D9CE4CBE-C8C3-4203-A58B-7CF7B830880E}&k="+str(ingred1)
        ing_webpage = requests.get(ingIngred, headers=HEADERS)
        ing_soup = BeautifulSoup(ing_webpage.content, "lxml")
        ingPirce = ing_soup.find_all('div', class_="text--small")[0]
        print(ingPirce)

        metroIngred = "https://www.metro.ca/en/search?filter="+str(ingred1)
        metro_webpage = requests.get(metroIngred, headers=HEADERS)
        metro_soup = BeautifulSoup(metro_webpage.content, "lxml")
        metroPirce = metro_soup.find_all('div',class_="pricing__secondary-price")[0]
        print(metroPirce)

        
        #return ingPirce
    return render_template('index.html')


    if request.method == 'POST':
        # ingred1 = request.form.get('ingred1')
        provIng1 = "https://www.provigo.ca/search?search-bar=chicken"
        # provIng1 = "https://www.provigo.ca/search?search-bar="+str(ingred1)
        # print(provIng1)
        r1 = requests.get(provIng1)
        # r1T = r1.text
        # print(r1T)

        # soup1 = BeautifulSoup(r1.content, 'html.parser')
        soup1 = BeautifulSoup(r1.content, 'lxml')
        print(list(soup1)[-1000:])

        # price = soup1.find_all("span",class_="price__value")
        # price = soup1.find("span",class_="price__value")
        price = soup1.find("div",class_="ad-unit-link-wrapper")
        print(price)

        # ingred2 = request.form.get('ingred2')
        # provIng2 = "https://www.provigo.ca/search?search-bar="+ingred2
        # r2 = requests.get(provIng2)
        print("in if")
        return provIng1
        
    print("bruh")
    return render_template('index.html')

# @app.route("/ingreds", method = ['GET', 'POST'])
# def ingreds():
#     return render_template('ingredients.html')

if __name__ == "__main__":
    app.run()