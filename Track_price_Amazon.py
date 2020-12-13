import requests
from bs4 import BeautifulSoup
import smtplib #enable to send emial
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="URL of Amazon product", type=str)
parser.add_argument("-s", "--sender", help="Sender email addres (Gmail)", type=str)
parser.add_argument("-ps", "--password", help="Password of sender", type=str)
parser.add_argument("-r", "--receiver", help="Reciver email addres", type=str)
parser.add_argument("-ua", "--userAgent", help="Your user agent", type=str)
parser.add_argument("-pr", "--price", help="Price of the item, which is affordable for you", type=float)

args = parser.parse_args()

URL = args.url
headers = {"User-Agent": args.userAgent}


def convert_price(price):
    
    converted_price = price.replace(u'\xa0', '').replace(' ', '').replace(',','.')
    converted_price = float(converted_price[0:-1])
    
    return converted_price
    
def check_price():
    
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    converted_price = convert_price(price)

    if(converted_price<float(args.price)):
        send_mail()
        
        return True
    
    else:
        return False

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #estblish connection bettwen two emails
    server.starttls()
    server.ehlo()
   
    server.login(args.sender, args.password)
   
    subject =  'Price fell down!'
    body = 'Check the Amaozn link {}'.format(args.url)
    
    msg = f'Subject: {subject}\n\n{body}'
    
    server.sendmail(
        args.sender,
        args.receiver,
        msg=msg
    )
    print('Email has been send')
          
          
if __name__ == "__main__":
    while True:
        if(check_price()):
            break 
        time.sleep(60*60*6) # check one time per 6 hours  
