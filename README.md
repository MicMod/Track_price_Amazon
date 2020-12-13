# Script to track Amazon prices 
The script tracks the price of an item on Amazon site. If the price is lower than defined as the argument, you will receive a mail. 
## What you need to do before running the script?

To send the email alert you need to do the 2-step verification of your Google account: <br />
1. Go to https://www.google.com/landing/2step/
2. Enable the 2-step verification
3. Now you can set a password for the app. Go to Google Account and search "google app password" 
![Screenshot](app_password.png)
4. Click "Generate"
5. Copy the password from a pop-up window and use it in the argument *--password*<br />

## How to use?
To run the script you need to type in console:
```bash
python Track_price_Amazon.py --url "URL of Amazon product" --sender "sender's Gmail address" --password "sender's password" --receiver "receiver's email" --userAgent "your user agent" --price 9999
```
### What means arguments?
- **--url** - addres URL of Amazon product <br />
Exmaple: <br />
--ulr "https://www.amazon.de/-/pl/dp/B07XRR92LP/ref=zg_bs_3468301_23?_encoding=UTF8&psc=1&refRID=MBW4BYQD03MMZXZA2WD4" <br />

- **--sender** - sender's gmail address - 2-step verification of Google account is needed <br />
Example: <br />
-- sender "sender___mail@gmail.com"

- **--password** sender's password for the application. Look at points 3-5 *What you need to do before running the script?* <br />
Example: <br />
-- password "passworddddddddd" <br />

- **receiver**  - receiver's email address - this is the email on which you will receive alerts <br />
Example: <br />
-- receiver "receiver___mail@wp.pl <br />

- **--userAgent** - your user agent - to  get this type in Google browser "my user agent"
Example: <br />
-- userAgent "Mozilla/x.x (X11; Linux x86_xx) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx" <br />

- **--price**  - the price which is affordable for you -  if the actual price on Amazon is lower, you will receive the mail. <br />
Example: <br />
-- price 1010 


