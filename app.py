from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Cat App'

