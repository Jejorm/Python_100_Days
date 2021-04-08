import smtplib
from random import randint
import pandas as pd
from datetime import datetime


my_email = "example@gmail.com"
my_password = "apassword"

today = (datetime.now().month, datetime.now().day)

birthday_data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
