import os
import requests
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ["APIKEY"]
DOMAIN = os.environ["DOMAIN"]
url = f"https://api.mailgun.net/v3/{DOMAIN}/messages"
auth = ("api", APIKEY)

data = {
    "from": "umitaslan_resume@mailgun.org",
    "to": ["aslan.umit@outlook.com"],
    "subject": "NEW MESSAGE FROM YOUR WEBSITE",
    "text": "TEST MAIL"}

response = requests.post(url=url, auth=auth, data=data)
print(response.text)
