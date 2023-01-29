from flask import Flask, redirect, url_for, render_template, request
from bs4 import BeautifulSoup
import requests
import utilities
import string

def parser(ingredients):
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    ing_list = ingredients.split()

    for i in ing_list:

        print("For: " + i)

        igaIngred = "https://www.iga.net/en/search?t={D9CE4CBE-C8C3-4203-A58B-7CF7B830880E}&k="+str(i)
        ing_webpage = requests.get(igaIngred, headers=HEADERS)
        iga_soup = BeautifulSoup(ing_webpage.content, "lxml")
        try:
            igaPirce = iga_soup.find_all('div', class_="text--small")[0]
            igaPriceS = str(igaPirce)
            print("IGA's price is: "+str(igaPriceS))
        except IndexError:
            print("")

        metroIngred = "https://www.metro.ca/en/search?filter="+str(i)
        metro_webpage = requests.get(metroIngred, headers=HEADERS)
        metro_soup = BeautifulSoup(metro_webpage.content, "lxml")
        try:
            metroPirce = metro_soup.find_all('div',class_="pricing__secondary-price")[0]
            metroPirceS = str(metroPirce)
            print("Metro's price is: "+ str(metroPirceS))

        except IndexError:
            print("")  

        provIngred = "https://www.provigo.ca/search?search-bar="+str(i)
        prov_webpage = requests.get(provIngred, headers=HEADERS)
        prov_soup = BeautifulSoup(prov_webpage.content, "lxml")
        try:

            provPirce = prov_soup.find_all('ul',class_="comparison-price-list comparison-price-list--product-tile")[0]
            provPirce = str(provPirce)
            print("Provigo's price is: "+str(provPirce))
        except IndexError:
            print("")     

def extract_price(someString):
    price = ""
    for i in someString:
        if i.isdigit():
            price += i 
    return price     

print(extract_price("Saad123"))    
