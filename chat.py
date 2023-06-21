import openai
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')