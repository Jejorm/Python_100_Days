import smtplib
import datetime as dt
from random import choice


now = dt.datetime.now()
weekday = now.weekday()

my_email = "example@gmail.com"
my_password = "apassword"
receiver_email = "receiverexample@yahoo.com"

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject:Quote\n\n{quote}."
        )
