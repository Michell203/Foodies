from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home(): #home page
    # if request.method == 'POST':
    #     HEADERS = ({'User-Agent':
    #         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    #         'Accept-Language': 'en-US, en;q=0.5'})

            
    #     URL = "https://www.iga.net/en/online_grocery/browse/Meat/Fresh%20Chicken%20&%20Fowl/Chicken%20&%20Fowl%20Prepared%20Vendor"
    #     webpage = requests.get(URL, headers=HEADERS)
    #     soup = BeautifulSoup(webpage.content, "lxml")
    #     # Outer Tag Object

    #     # title = soup.find("span", attrs={"id":'productTitle'})
    #     print(soup.find_all('div', class_="text--small"))
    #     # Inner NavigableString Object
    #     # title_value = title.string
    #     # Title as a string value
    #     # title_string = title_value.strip()
    #     # Printing types of values for efficient understanding
    #     # print(type(title))
    #     # print(type(title_value))
    #     # print(type(title_string))
    #     print()

    #     # Printing Product Title
    #     # print("Product Title = ", title_string)
    # return render_template('index.html')


    if request.method == 'POST':
        HEADERS = ({'User-Agent':
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
             'Accept-Language': 'en-US, en;q=0.5'})

        ingred1 = request.form.get('ingred1')
        ingIng1 = "https://www.iga.net/en/search?t=%7B14A91276-40BA-49D5-940D-3692DE3DC381%7D&k="+str(ingred1)
        ing = requests.get(ingIng1)

        ingPage = requests.get(ing)
        ingSoup = BeautifulSoup(ingPage.content, "lxml")
        # r1T = r1.text
        # print(r1T)

        # soup1 = BeautifulSoup(r1.content, 'html.parser')
        print(ingSoup.find_all('div', class_="text--small")[0])

        # price = soup1.find_all("span",class_="price__value")
        # price = soup1.find("span",class_="price__value")
        # print(price)

        # ingred2 = request.form.get('ingred2')
        # provIng2 = "https://www.provigo.ca/search?search-bar="+ingred2
        # r2 = requests.get(provIng2)
        print("in if")
        return ingSoup
        
    print("bruh")
    return render_template('index.html')

# @app.route("/ingreds", method = ['GET', 'POST'])
# def ingreds():
#     return render_template('ingredients.html')

if __name__ == "__main__":
    app.run()