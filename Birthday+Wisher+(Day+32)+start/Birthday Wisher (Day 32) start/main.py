import smtplib
import datetime as dt
now = dt.datetime.now()
import random
with open('quotes.txt') as quote_file:
    quote_list = quote_file.readlines()
    monday_quote = random.choice(quote_list)
if now:
    with smtplib.SMTP('smtp.gmail.com') as server:
        server.starttls()
        server.login('gen2proff@gmail.com', 'gen2;soul')
        server.sendmail('gen2proff@gmail.com','gen2proff@yahoo.com', msg=monday_quote)

