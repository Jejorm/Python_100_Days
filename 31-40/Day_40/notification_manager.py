import smtplib
from twilio.rest import Client
from os import environ

TWILIO_SID = environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = environ.get("AUTH_TOKEN")
TWILIO_VERIFIED_NUMBER = environ.get("TO_C")
# MAIL_PROVIDER_SMTP_ADDRESS = YOUR EMAIL PROVIDER SMTP ADDRESS "smtp.gmail.com"
MY_EMAIL = environ.get("EMAIl")
MY_PASSWORD = environ.get("EMAIL_PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="whatsapp:+14155238886",
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )