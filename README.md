# Script to track Amazon prices 
The script tracks the price of an item on Amazon site. If the price is lower than defined as an argument, you will receive a mail. 
## How to use?
To run the script you need to typ in console:
```bash
python Track_price_Amazon.py --url "URL of Amazon product" --sender "sender's gmail addres" --password "sender's password" --reciver "reciver's email" --userAgent "your user agent" --price 9999
```
### What means arguments?
- **--url** - addres URL of Amazon product - exmaple: *https://www.amazon.de/-/pl/dp/B07XRR92LP/ref=zg_bs_3468301_23?_encoding=UTF8&psc=1&refRID=MBW4BYQD03MMZXZA2WD4*
