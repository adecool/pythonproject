import requests

from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "6VM4YGCXBCI2DIQP"
NEWS_API_KEY = "e6c4f93a4a19447a808e8c19e2823df3"
ACCOUNT_SID = "AC70f6ba03952ae76e69134b79fd7c0a31"
AUTH_TOKEN = "e0b329a9481c0883253e04cb27ddab39"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]
yesterday_close_price = float(data_list[0]['4. close'])


day_before_yesterday_closing_price = float(data_list[1]['4. close'])

positive_difference = abs(yesterday_close_price - day_before_yesterday_closing_price)

percentage_difference = (positive_difference/yesterday_close_price) * 100
if percentage_difference > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles'][:3]
    formated_articles = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in articles]


    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_='+19704894858',
            to='+2349033234055',
        )
        print(message.sid)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

