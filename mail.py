import os
import requests
from dotenv import load_dotenv

load_dotenv()

# APIKEY = os.environ["APIKEY"]
# DOMAIN = os.environ["DOMAIN"]
# url = f"https://api.mailgun.net/v3/{DOMAIN}/messages"
# auth = ("api", APIKEY)
#
# data = {
#     "from": "umitaslan_resume@mailgun.org",
#     "to": ["aslan.umit@outlook.com"],
#     "subject": "NEW MESSAGE FROM YOUR WEBSITE",
#     "text": "TEST MAIL"}
#
# response = requests.post(url=url, auth=auth, data=data)
# print(response.text)

import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = To("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)