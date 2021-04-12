import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for key, value in stock_data.items()]

yesterday_stock = stock_data_list[0]
yesterday_close = float(yesterday_stock["4. close"])


day_before_yesterday_stock = stock_data_list[1]
day_before_yesterday_close = float(day_before_yesterday_stock["4. close"])

difference = round(abs(yesterday_close - day_before_yesterday_close), 2)

up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"


difference_percentage = round((difference / yesterday_close) * 100)

if abs(difference_percentage) > 0:
    parameters_2 = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    response_2 = requests.get(NEWS_ENDPOINT, params=parameters_2)
    response_2.raise_for_status()

    news_articles = response_2.json()["articles"]
    three_articles = news_articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{difference_percentage}%\n\n"
                          f"Headline: {article['title']}. \n\nBrief: {article['description']}\n\n"
                          for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    from_whatsapp_number = "whatsapp:+14155238886"
    to_whatsapp_number = os.environ.get("TO_C")

    for article in formatted_articles:
        message = client.messages.create(body=article,
                                         from_=from_whatsapp_number,
                                         to=to_whatsapp_number,
                                         )
        print(message.status)
