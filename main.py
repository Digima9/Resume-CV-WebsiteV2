import datetime
import smtplib
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
import pprint
import requests

import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, InputRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 
    
On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['GET','POST'])
def contact_me():

    if request.method == "POST":
        name = request.form['name']
        contact_email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        print(name, contact_email, subject, message)

        load_dotenv()
        email = "umitaslan.au@gmail.com"
        email_to2 = "aslan.umit@outlook.com"

        pprint.pprint(dict(os.environ))
        password = os.environ["PASSWORD"]
        # load_dotenv()
        #
        # APIKEY = os.environ["APIKEY"]
        # DOMAIN = os.environ["DOMAIN"]
        # url = f"https://api.mailgun.net/v3/{DOMAIN}/messages"
        # auth = ("api", APIKEY)
        #
        # data = {
        #     "from": "umitaslan_resume@mailgun.org",
        #     "to": ["aslan.umit@outlook.com"],
        #     "subject": "NEW MESSAGE FROM YOUR WEBSITE",
        #     "text": f"Subject: {subject}\n\nMessage From : {name}\n\nEmail Address:{contact_email}\n\nMessage :{message}"}
        #
        # response = requests.post(url=url, auth=auth, data=data)
        # print(response.text)

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:

            connection.starttls()
            connection.login(user=email, password=password)

            connection.sendmail(from_addr=email, to_addrs=email_to2,
                                msg=f'Subject:An email from your site-Subject: {subject}'
                                    f'\n\nMessage From : {name}\n\n'
                                    f'Email Address:{contact_email}\n\nMessage :{message}')

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
