import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
from os import environ

AMAZON_PRODUCT = "AMAZON LINK OF PRODUCT"

# Page for headers
# http://myhttpheader.com/
ACCEPT_LANGUAGE = "LANGUAGE HEADER"
USER_AGENT = "USER AGENT HEADER"

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

EMAIL = environ.get('GMAIL')
EMAIL_PASSWORD = environ.get('GMAIL_PASSWORD')

MAX_PRICE = 0 #Max price to receive alert

response = requests.get(AMAZON_PRODUCT, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").getText()
price_formatted = float(price.split("$")[1])

title = soup.find(id="productTitle").getText().strip()

if price_formatted <= MAX_PRICE:
    message = f"{title} is now ${price_formatted}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_PRODUCT}"
        )
