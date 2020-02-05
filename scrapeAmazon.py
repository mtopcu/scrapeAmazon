import requests
import time, sys
from bs4 import BeautifulSoup

def convertPrice(price): # to convert unicode price data to float type
    prc = []
    for i in price:
        if i.isdigit():
	    prc.append(i)
	
    prc.insert(-2, '.')
    prc = float(''.join(prc))
    return prc


def checkPrice(url, target_price):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
	
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
	
    if convertPrice(price) <= target_price:
        print("Product price is getting down!")
	


url = "https://www.amazon.co.uk/KINGZ-Classic-Mens-Jitsu-Kimono/dp/B07V6ZFYG3"
target_price = 75


while True:
    checkPrice(url, target_price)
    time.sleep(900) # Checks in each 15 minutes.
