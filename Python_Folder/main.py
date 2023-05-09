from flask import Flask, render_template, request, session
import requests
from replit import db
import os

app = Flask(__name__)

app.secret_key = os.environ['flask_secret_key']

app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

if 'total_emails_sent' not in db:
    db['total_emails_sent'] = 0

if 'last_email' not in db:
    db['last_email'] = ''

if 'users' not in db:
    db['users'] = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('Login/Signup Button Clicked!!')
