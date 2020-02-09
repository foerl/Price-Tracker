import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/ROG-Strix-RTX2080TI-A11G-Gaming-Grafikkarte-Nvidia-Speicher-Displayport/dp/B07HNRKP7Z/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=2080ti&qid=1581248994&sr=8-5'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.000):
        send_mail()

    print(converted_price)
    print(title.strip())

    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('SEND@gmail.com', 'PASSWORD')

    subject = 'Price just fell!'
    body = 'Check the price here: https://www.amazon.de/ROG-Strix-RTX2080TI-A11G-Gaming-Grafikkarte-Nvidia-Speicher-Displayport/dp/B07HNRKP7Z/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=2080ti&qid=1581248994&sr=8-5'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SEND@gmail.com',
        'RECEIVE@gmail.com',
        msg
    )
    print('Email has been sent')

    server.quit()

#import time module
import time
t = 60000 # 60000 seconds equals 16.67 hours

while(True):
    check_price()
    time.sleep(t)
