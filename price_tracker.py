import requests 
from bs4 import BeautifulSoup
import csv
from datetime import datetime

URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_price():
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("p", class_ = "price_color").text.strip()
    return float(price.replace("£","").replace("Â",""))

def save_price(price):
    with open("prices.csv", "a", newline ="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(),price])

def check_alert(price,threshold=60.0):
    if price < threshold:
        print(f"ALERT: Price dropped to £ {price}!")
    else: 
        print(f"Current price: £{price} - no alert.")

price = get_price()
save_price(price)
check_alert(price)